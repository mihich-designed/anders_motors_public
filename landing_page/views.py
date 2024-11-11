from django.shortcuts import render, redirect
from django.views import View
from .forms import UserContactsForm, UserContactsForm2
from django.http import JsonResponse



# Create your views here.

class UserContactsView(View):
    def get(self, request):
        form = UserContactsForm()
        form2 = UserContactsForm2()
        return render(request, 'index.html', {
            'form': form,
            'form2': form2,
        })
    def post(self, request):
        form = UserContactsForm(request.POST)
        form2 = UserContactsForm2(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        elif form2.is_valid():
            form2.save()
            return JsonResponse({'success': True})
        return JsonResponse({'errors': {**form.errors, **form2.errors}}, status=400)
