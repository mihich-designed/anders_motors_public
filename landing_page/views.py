from django.shortcuts import render, redirect
from django.views import View
from .forms import UserContactsForm
from django.http import JsonResponse
import bleach


# Create your views here.

def main_page(request):
    return render(request, 'main_page.html')

class UserContactsView(View):
    def get(self, request):
        form = UserContactsForm()
        return render(request, 'includes/user_contacts_form.html', {'form': form})
    def post(self, request):
        form = UserContactsForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        return render(request, 'includes/user_contacts_form.html', {'form': form})