from django.shortcuts import render, redirect
from django.views import View
from .forms import UserContactsForm
from .models import UserContacts
from django.conf import settings

# Create your views here.

def main_page(request):
    return render(request, 'main_page.html')

class UserContactsView(View):
    def get(self, request):
        form = UserContactsForm()
        return render(request, 'includes/user_contacts_form.html', context={
            'form': form,
        })
    def post(self, request):
        form = UserContactsForm(request.POST, instance=request.usercontacts)
        if form.is_valid():
            form.save()
            return redirect('main-page')
        return render(request, 'includes/user_contacts_form.html', context={
            'form': form,
        })