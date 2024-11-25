
from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('registration', views.registration, name='registration'),
    path('about', views.about, name='about'),
    path('MilkCollection', views.milk_collection_view , name="MilkCollection"),
    path('milk_collection_list', views.milk_collection_list, name="milk_collection_list"),
    
]
