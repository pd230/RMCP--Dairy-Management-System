from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import MilkOrder

class FarmerRegistrationForm(UserCreationForm):
    
    phone_no = forms.CharField(max_length=15, required=True)
    address  = forms.CharField(widget=forms.Textarea, required=True)
    
    class Meta:
        model = User # Specify the User model
        
        fields = ['first_name','last_name','username','email','password1','password2','phone_no','address'] # Include desired fields
    


class MilkOrderForm(forms.ModelForm):
    class Meta:
        model = MilkOrder
        fields = ['quantity']  # Add other fields if required
        widgets = {
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity in liters'}),
        }