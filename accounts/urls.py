from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # path('registration', views.registration, name="registration"),
    path('venderlogin', views.venderlogin, name="venderlogin"),
    path('userDashBoard', views.userDashBoard, name="userDashBoard"),
    path('userDashBoard', views.user_profile, name="userDashBoard"),
    path('logout', views.logout, name="logout"),
    path('register_milk_vendors', views.register_milk_vendors, name="register_milk_vendors"), 
    path('user_profile', views.user_profile, name="user_profile"),   
    path('adminDashboard', views.adminDashboard, name="adminDashboard"),   
    path('adminlogin', views.adminlogin, name="adminlogin"), 
    path('PriceChart', views.PriceChart, name="PriceChart"),
    path('register_milk_Purchaser', views.register_milk_Purchaser, name="register_milk_Purchaser"),
    path('Purchaserlogin', views.Purchaserlogin, name="Purchaserlogin"),
]
