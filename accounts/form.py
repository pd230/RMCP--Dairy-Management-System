from django import forms
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import MilkBuyer, MilkOrder, MilkSeller


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")


class FarmerRegistrationForm(forms.ModelForm):
     class Meta:
        model = MilkSeller
        fields = ['phone_no','address', 'name']

class MilkBuyerForm(forms.ModelForm):
    class Meta:
        model = MilkBuyer
        fields = ['name', 'companyname', 'prn', 'address']


class MilkOrderForm(forms.ModelForm):
    class Meta:
        model = MilkOrder
        fields = ['quantity']  # Add other fields if required
        # widgets = {
        #     'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity in liters'}),
        # }