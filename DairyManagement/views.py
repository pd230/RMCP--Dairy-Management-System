from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import MilkCollection, milk_pricing
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# Create your views here.
def milk_collection_view (request):
    if request.method == "POST": 
        username = request.POST.get("Username")
        grade = request.POST.get("grade")
        Quantity = request.POST.get("Quantity")
        try: 
        # Validate and fetch user and pricing
            user = User.objects.get(username=username)  # Ensure the user exists
            pricing = milk_pricing.objects.get(grade = grade)
        
            MilkCollection.objects.create(
                user=user,
                grade=pricing,
                liters_collected=float(Quantity),  # Convert to float
            )
            return redirect('milk_collection_list')  # Redirect to the same view after submission
        
            # Fetch all collections to display
            # collections = MilkCollection.objects.all()
            # return render(request, 'milk_collection_list.html', {'collections': collections})
    
        except User.DoesNotExist:
            return HttpResponseNotFound("User not found!")
        except milk_pricing.DoesNotExist:
            return HttpResponseNotFound("Milk pricing not found!")
        except Exception as e:
            return HttpResponseNotFound(f" error occurs : {str(e)}")
        
    else:
        return render(request, "milkCollection.html")
    
    
def milk_collection_list(request):
    # Fetch all milk collections
    collections = MilkCollection.objects.all()
    return render(request, "milk_collection_list.html", {'collections': collections})

def index(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")

def registration(request):
    return render(request, "registration.html")

def about(request):
    return render(request, "about.html")


@csrf_exempt
def send_email(request):
    if request.method == "POST":
        # Get form data
        sender_name = request.POST.get('name')
        sender_email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Admin's email
        admin_email = "pratikshadixit233@gmail.com"

        # Create the email body
        email_body = f"Sender Name: {sender_name}\nSender Email: {sender_email}\n\nMessage:\n{message}"

        try:
            # Send email
            send_mail(
                subject=subject,
                message=email_body,
                from_email=sender_email,  # Use sender's email dynamically
                recipient_list=[admin_email],
                fail_silently=False,
            )
            return JsonResponse({"status": "success", "message": "Email sent successfully!"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": f"Failed to send email: {str(e)}"})

    return JsonResponse({"status": "error", "message": "Invalid request method"})
