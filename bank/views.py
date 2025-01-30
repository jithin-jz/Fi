from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile, BankAccount, Transaction, BankCard
from .forms import ProfileForm, SendMoneyForm

@login_required
def home(request):
    user = request.user
    bank_account = get_object_or_404(BankAccount, user=user)
    profile = get_object_or_404(Profile, user=user)
    transactions = Transaction.objects.filter(account=bank_account).order_by('-created_at')
    bank_cards = BankCard.objects.filter(account=bank_account)
    
    profile_form = ProfileForm(request.POST or None, instance=profile)
    if request.method == 'POST' and 'profile_submit' in request.POST:
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('home')
    
    send_money_form = SendMoneyForm(request.POST or None, initial={'user_id': user.id})
    if request.method == 'POST' and 'send_money_submit' in request.POST:
        if send_money_form.is_valid():
            recipient = send_money_form.cleaned_data['recipient']
            amount = send_money_form.cleaned_data['amount']
            description = send_money_form.cleaned_data['description']
            
            recipient_account = get_object_or_404(BankAccount, user=recipient)
            sender_account = bank_account
            
            if sender_account.balance >= amount:
                sender_account.balance -= amount
                recipient_account.balance += amount
                sender_account.save()
                recipient_account.save()
                
                Transaction.objects.create(account=sender_account, recipient=recipient, transaction_type='debit', amount=amount, description=description)
                Transaction.objects.create(account=recipient_account, recipient=user, transaction_type='credit', amount=amount, description=description)
                
                messages.success(request, f'Successfully sent {amount} to {recipient.username}!')
                return redirect('home')
            else:
                send_money_form.add_error('amount', 'Insufficient balance')
                messages.error(request, 'Insufficient balance to complete the transaction.')
    
    context = {
        'bank_account': bank_account,
        'profile': profile,
        'transactions': transactions,
        'bank_cards': bank_cards,
        'profile_form': profile_form,
        'send_money_form': send_money_form,
    }
    return render(request, 'home.html', context)
