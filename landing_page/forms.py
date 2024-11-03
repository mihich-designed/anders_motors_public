from django import forms
from .models import UserContacts

class UserContactsForm(forms.ModelForm):
    class Meta:
        model = UserContacts
        fields = ['name', 'phone_number']
        labels = {
            'name': 'Ваше имя',
            'phone_number': 'Телефон',
        }


    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        phone_number = str(cleaned_data.get('phone_number'))
        if len(phone_number) > 12 or len(phone_number) < 11:
            raise forms.ValidationError(f'Запишите свой номер в формате: 79998885577')

        elif len(name) > 20:
            raise forms.ValidationError(f'Слишком длинное имя')
