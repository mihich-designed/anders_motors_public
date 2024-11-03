from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.UserContactsView.as_view(), name='user-contacts-views'),
]