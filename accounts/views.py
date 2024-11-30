from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User , auth
from .models import MilkOrder, milk_pricing, milk_vendors,MilkBuyer
from .form import FarmerRegistrationForm, MilkBuyerForm, MilkOrderForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login
from django.contrib.auth import authenticate


# Create your views here.

def register_milk_vendors(request):
    if request.method == 'POST':
        form = FarmerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            phone_no = form.cleaned_data['phone_no']
            address = form.cleaned_data['address']
            milk_vendors.objects.create(user=user, phone_no=phone_no, address=address)
            return redirect('venderlogin')  # Redirect to the login page
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
    


def user_profile(request):
    vendor_details = None
    if request.user.is_authenticated:
        try:
            vendor_details = milk_vendors.objects.get(user=request.user)
        except milk_vendors.DoesNotExist:
            vendor_details = None
    
    context = {
        'user': request.user,
        'vendor_details': vendor_details
    }
    return render(request, 'userDashBoard.html', {'user': request.user, 'vendor_details': vendor_details})


def adminlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_superuser:
                auth.login(request, user)
                messages.success(request,"successfully login")
                return redirect("adminDashboard")
            else:
                messages.error(request,"Not aunthenticated Admin")
        else:
            messages.error(request,"admin not found")
            return redirect("adminlogin")
        
    else:
        return render(request, "adminlogin.html")
    
    
    

def userDashBoard(request):
    return render(request, 'userDashBoard.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def adminDashboard(request):
    return render(request, "adminDashboard.html")

def PriceChart(request):
    pricing_data = milk_pricing.objects.all()
    return render(request, "PriceChart.html", {'pricing_data': pricing_data})
    

def Purchaserlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Fetch the MilkBuyer object using the username
        try:
            milk_buyer = MilkBuyer.objects.get(username=username)
            if milk_buyer.user is None:
                messages.error(request, 'No associated user found for this MilkBuyer')
                return render(request, 'Purchaserlogin.html')

            # Get the associated User object
            user = milk_buyer.user  # This is the User object related to MilkBuyer

            # Authenticate and log in the user
            user = authenticate(username=user.username, password=password)
            if user is not None:
                login(request, user)  # Django's login function
                return redirect('BuyersDashBoard')  # Redirect to the home page after successful login
            else:
                messages.error(request, 'Invalid username or password')
        except MilkBuyer.DoesNotExist:
            messages.error(request, 'No such MilkBuyer found')

    return render(request, 'Purchaserlogin.html')


def register_milk_Purchaser(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        milkbuyer_form = MilkBuyerForm(request.POST)
        if user_form.is_valid() and milkbuyer_form.is_valid():
            # Create user
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            # Create MilkBuyer
            milk_buyer = milkbuyer_form.save(commit=False)
            milk_buyer.user = user
            milk_buyer.username = user.username
            milk_buyer.save()
            messages.success(request, "Registration successful!")
            return redirect('Purchaserlogin')
    else:
        user_form = UserRegistrationForm()
        milkbuyer_form = MilkBuyerForm()
    return render(request, 'register_milk_Purchaser.html', {'user_form': user_form, 'milkbuyer_form': milkbuyer_form})


def milk_buyer_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        try:
            buyer = MilkBuyer.objects.get(username=username)
            if check_password(password, buyer.password):
                messages.success(request, f"Welcome, {buyer.name}!")
                return redirect('buyer_dashboard')  # Replace with your dashboard URL
            else:
                messages.error(request, "Invalid credentials!")
        except MilkBuyer.DoesNotExist:
            messages.error(request, "User does not exist!")

    return render(request, 'Purchaserlogin.html')

def BuyersDashBoard(request):
    return render(request, "BuyersDashBoard.html")


@login_required
def place_order(request):
    if request.method == 'POST':
        form = MilkOrderForm(request.POST)
        if form.is_valid():
            try:
                # Fetch the logged-in user's MilkBuyer profile
                milkbuyer = request.user.milkbuyer
                order = form.save(commit=False)
                order.buyer = milkbuyer
                order.save()
                messages.success(request, "Order placed successfully!")
                return redirect('BuyersDashBoard')
            except MilkBuyer.DoesNotExist:
                messages.error(request, "MilkBuyer profile not found for the logged-in user.")
    else:
        form = MilkOrderForm()

    return render(request, 'place_order.html', {'form': form})

def admin_buying_requests(request):
    orders = MilkOrder.objects.all().order_by('-request_date')  # Display latest requests first
    return render(request, 'admin_buying_requests.html', {'orders': orders})