from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import BankAccount, Profile,BankCard

@receiver(post_save, sender=User)
def create_user_related_data(sender, instance, created, **kwargs):
    """Create related BankAccount, Profile, and BankCard for the user."""
    if created:
        # Create BankAccount only if it doesn't exist for the user
        if not hasattr(instance, 'bank_account'):
            bank_account = BankAccount.objects.create(user=instance)
        
        # Create Profile if it doesn't already exist
        if not hasattr(instance, 'profile'):
            Profile.objects.create(user=instance)
        
        # Create a BankCard linked to the BankAccount
        if not hasattr(instance, 'bankcard'):
            BankCard.objects.create(account=bank_account)

@receiver(post_save, sender=User)
def save_user_related_data(sender, instance, **kwargs):
    """Save related BankAccount and Profile when the User is saved."""
    if hasattr(instance, 'bank_account'):
        instance.bank_account.save()
    if hasattr(instance, 'profile'):
        instance.profile.save()

