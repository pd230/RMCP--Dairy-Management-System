from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # path('registration', views.registration, name="registration"),
    path('venderlogin', views.venderlogin, name="venderlogin"),
    path('userDashBoard', views.userDashBoard, name="userDashBoard"),
    path('logout', views.logout, name="logout"),
    path('register_milk_vendors', views.register_milk_vendors, name="register_milk_vendors")    
]
