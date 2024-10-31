from django.shortcuts import render
from django.views import View
from .forms import UserContactsForm
from .models import UserContacts
from django.conf import settings

# Create your views here.

class MainPageView(View):

    def get(self, request):
        form = UserContactsForm()
        BASE_DIR = settings.BASE_DIR
        return render(request, 'base.html', context={
            'form': form,
            'BASE_DIR': BASE_DIR,
        })

    def post(self, request):
        form = UserContactsForm(request.POST, instance=request.usercontacts)
        if form.is_valid():
            form.save()
        return render(request, 'base.html', context={
            'form': form,
        })