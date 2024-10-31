from django.db import models

# Create your models here.

class UserContacts(models.Model):
    """Хранит контактные данные клиентов"""
    name = models.CharField(max_length=20)
    phone_number = models.IntegerField()
