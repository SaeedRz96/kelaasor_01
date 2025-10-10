from django.db.models.signals import post_save
from user_app.models import Transaction, Wallet
from django.dispatch import receiver

@receiver(post_save, sender=Transaction)
def update_wallet_amount(sender, instance, created, **kwargs):
    if created:
        wallet = Wallet.objects.get(user=instance.user)
        if instance.payment_type == 'a':
            wallet.amount = wallet.amount + instance.amount
            wallet.save()
        elif instance.payment_type == 'b':
            wallet.amount = wallet.amount - instance.amount
            wallet.save()    
