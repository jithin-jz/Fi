from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from bank.views import *
from bank.models import *

@login_required(login_url='signup')
def home(request):
    bank_account = BankAccount.objects.filter(user=request.user).first()
    context = {
            'bank_account': bank_account,
        }
    return render(request, 'home.html',context)

def signup_view(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'signup':
            username = request.POST.get('username')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')

            if password1 != password2:
                messages.error(request, 'Passwords do not match!')
                return redirect('signup')

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('signup')

            user = User.objects.create_user(username=username, password=password1)
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')

        elif form_type == 'login':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Logged in successfully!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password!')
                return redirect('signup')

    return render(request, 'signup.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Logged out successfully!')
    return redirect('signup')

