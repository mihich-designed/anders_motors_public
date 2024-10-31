from django import forms
from .models import UserContacts

class UserContactsForm(forms.ModelForm):
    class Meta:
        model = UserContacts
        fields =['name', 'phone_number']
        widgets = {
            'name': forms.TextInput(attrs={'label': 'Ваше имя'}),
        }