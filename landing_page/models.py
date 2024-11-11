from django.db import models

# Create your models here.

class UserContacts(models.Model):
    """Хранит контактные данные клиентов"""
    name = models.CharField(max_length=20)
    phone_number = models.IntegerField()

    def __str__(self):
        return f'{self.name}: {self.phone_number}'

