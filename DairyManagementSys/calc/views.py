from django.http import HttpResponse
from django.shortcuts import render
from .models import Destination

# Create your views here.
def home(request):
    desc1 = Destination()
    desc1.name = "Mumbai"
    desc1.img = "animal.png"
    desc1.offer = False
    
    desc2  = Destination()
    desc2.name = "satara"
    desc2.img = "animal.png"
    desc2.offer = True
    
    list = [desc2, desc1]
    # directly passing data
    # return render(request, 'home.html',{'name' : 'pd'})
    # passing data via object 
    return render(request, 'home.html',{'desc' : list})
    


# def add(request):
    
#     val1 = int(request.POST["num1"])
#     val2 = int(request.POST["num2"])
#     res = val1 + val2
    
#     return render(request, 'result.html', {"result" : res})