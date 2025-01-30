import random
import string
from datetime import datetime
from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import forms

# Utility Functions
def generate_random_digits(length):
    return ''.join(random.choices(string.digits, k=length))

def generate_random_upi_id(username):
    return f"{username.lower()}@fi"

def generate_random_cvv():
    return generate_random_digits(3)

def generate_random_expiry_date():
    month = random.randint(1, 12)
    year = datetime.now().year % 100 + random.randint(1, 5)
    return f"{month:02}/{year}"

def generate_ifsc_code():
    return ''.join(random.choices(string.ascii_uppercase, k=4)) + '0' + generate_random_digits(3)

def generate_account_number():
    return generate_random_digits(15)

def generate_card_number():
    return generate_random_digits(16)

# Models
class BankAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='bank_account')
    account_number = models.CharField(max_length=15, unique=True, default=generate_account_number)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('1000.00'))
    ifsc_code = models.CharField(max_length=11, default=generate_ifsc_code)
    upi_id = models.CharField(max_length=50, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.upi_id:
            self.upi_id = generate_random_upi_id(self.user.username)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}'s Account"

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('credit', 'Credit'),
        ('debit', 'Debit'),
    )
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name='transactions')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_transactions', null=True, blank=True)
    transaction_type = models.CharField(max_length=6, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.transaction_type == 'debit':
            return f"Sent {self.amount} to {self.recipient.username} on {self.created_at}"
        else:
            return f"Received {self.amount} from {self.account.user.username} on {self.created_at}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class BankCard(models.Model):
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name='cards')
    card_number = models.CharField(max_length=16, unique=True, default=generate_card_number)
    cvv = models.CharField(max_length=3, default=generate_random_cvv)
    expiry_date = models.CharField(max_length=5, default=generate_random_expiry_date)
    is_active = models.BooleanField(default=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('10000.00'))

    def __str__(self):
        return f"Card **** **** **** {self.card_number[-4:]}"



