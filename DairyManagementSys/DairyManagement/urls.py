
from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('adminTable', views.adminTable, name='adminTable'),
    path('registration', views.registration, name='registration'),
    path('about', views.about, name='about'),
]
