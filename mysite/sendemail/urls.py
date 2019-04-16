from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.emailView, name='email'),
    path(r'success/', views.successView, name='success'),
]
