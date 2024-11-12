from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from telegram_bot.telegram_bot import send_contact_to_telegram
# Create your models here.

class UserContacts(models.Model):
    """Хранит контактные данные клиентов"""
    name = models.CharField(max_length=20)
    phone_number = models.IntegerField()

    def __str__(self):
        return f'{self.name}: {self.phone_number}'

@receiver(signals.post_save, sender=UserContacts)
def send_contact_to_bot(sender, instance, created, **kwargs):
    if created:
        # Передача новых контактов в тг-бота
        send_contact_to_telegram(instance.name, instance.phone_number)