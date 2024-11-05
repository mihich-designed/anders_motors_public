from django.shortcuts import render, redirect
from django.views import View
from .forms import UserContactsForm
from django.http import JsonResponse



# Create your views here.

class UserContactsView(View):
    def get(self, request):
        form = UserContactsForm()
        return render(request, 'main_page.html', {'form': form})
    def post(self, request):
        form = UserContactsForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        return JsonResponse({'errors': form.errors}, status=400)