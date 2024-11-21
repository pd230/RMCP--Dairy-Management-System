from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User , auth
from .models import milk_vendors
from django.shortcuts import render
from .form import FarmerRegistrationForm

# Create your views here.

# def registration(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
        
#         if password1 != password2:
#             messages.info(request, 'Passwords do not match.')
#             return redirect('registration')  # Redirect to registration page with error
        
#         # Check if username already exists
#         if User.objects.filter(username=username).exists():
#             messages.info(request, 'Username is already taken.')
#             return redirect('registration')
        
#         # Check if email already exists
#         if User.objects.filter(email=email).exists():
#             messages.info(request, 'Email is already in use.')
#             return redirect('registration')
        
#         # Create the user if everything is valid
#         user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
#         user.save()
#         print("user created successfully!")
#         messages.success(request, 'User created successfully. Please log in.')
#         return redirect('login')  # Redirect to login page (change this URL if needed)
    
#     # For GET requests, just render the registration page with an empty form
#     return render(request, 'registration.html')

def register_milk_vendors(request):
    if request.method == 'POST':
        form = FarmerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            phone_no = form.cleaned_data['phone_no']
            address = form.cleaned_data['address']
            milk_vendors.objects.create(user=user, phone_no=phone_no, address=address)
            return redirect('login')  # Redirect to the login page
    else:
        form = FarmerRegistrationForm()
    return render(request, 'register_milk_vendors.html', {'form': form})


def venderlogin(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request,"login succesfully!")
            return redirect('userDashBoard')
        else:
            messages.error(request,"invalid credentials")
            return redirect('venderlogin')
            
    else:
        return render(request, 'venderlogin.html')


def userDashBoard(request):
    return render(request, 'userDashBoard.html')

def logout(request):
    auth.logout(request)
    return redirect('/')