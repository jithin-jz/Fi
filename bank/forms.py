# forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Profile, BankAccount, Transaction, BankCard

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'email']

class SendMoneyForm(forms.Form):
    recipient = forms.ModelChoiceField(queryset=User.objects.all(), label="Recipient")
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    description = forms.CharField(max_length=255, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['recipient'].queryset = User.objects.exclude(id=self.initial.get('user_id'))