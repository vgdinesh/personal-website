from django.urls import path
from . import views
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'home/', views.index, name='index'),
    path(r'contact/', views.contact, name='contact'),
    path('resume/',views.resume, name='resume')
    ]
