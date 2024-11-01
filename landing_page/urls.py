from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_page, name='main-page'),
    path('', views.UserContactsView.as_view(), name='user-contacts-views'),
]