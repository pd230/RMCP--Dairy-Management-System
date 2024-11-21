from django.shortcuts import render

from .models import Destination



# Create your views here.

def index(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")

def registration(request):
    return render(request, "registration.html")

def adminTable(request):
    dest = Destination.objects.all()
    return render(request, "adminTable.html",{'dest' : dest})

def about(request):
    return render(request, "about.html")

