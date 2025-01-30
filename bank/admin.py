from django.contrib import admin
from .models import BankAccount, Transaction, Profile, BankCard

@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'account_number', 'balance', 'ifsc_code', 'upi_id')
    search_fields = ('user__username', 'account_number', 'upi_id')
    list_filter = ('ifsc_code',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account', 'transaction_type', 'amount', 'created_at', 'description')
    search_fields = ('account__account_number', 'transaction_type', 'description')
    list_filter = ('transaction_type', 'created_at')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'email')
    search_fields = ('user__username', 'phone_number', 'email')

@admin.register(BankCard)
class BankCardAdmin(admin.ModelAdmin):
    list_display = ('account', 'card_number', 'cvv', 'expiry_date')
    search_fields = ('card_number', 'account__account_number')
