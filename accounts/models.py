from django.db import models
from django.contrib.auth.models import User , auth

# Create your models here.
# model for vendors
class milk_vendors(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="milk_vendor")
    address = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=10, unique=True)
    join_date = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.user} - {self.address} - {self.phone_no} - {self.join_date}"
    
    


    
class milk_pricing(models.Model):
    
    QUALITY_CHOICES = [
        ('Premium', 'Premium'),
        ('Standard', 'Standard'),
        ('Organic', 'Organic'),
        ('Low-fat', 'Low-fat'),
        ('Full Cream', 'Full Cream'),
    ]

    GRADE_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]
    
    quality = models.CharField(max_length=20, choices=QUALITY_CHOICES)
    grade = models.CharField(max_length=1, choices=GRADE_CHOICES, unique=True)
    price_per_liter = models.DecimalField(max_digits=6, decimal_places=2)  # For accurate pricing
    last_updated = models.DateTimeField(auto_now=True)  # Automatically updates when saved

    def __str__(self):
        return f"{self.quality} - {self.grade} - {self.price_per_liter}"
    
    class Meta:
        verbose_name = "Milk Pricing"
        verbose_name_plural = "Milk Pricing"

    
    
    
# class milk_Buyers(models.Model):
#     name = models.CharField(max_length=50)
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=4)
#     companyname = models.CharField(max_length=50)
#     prn = models.IntegerField()
#     address = models.CharField(max_length=50)
    
#     def __str__(self) :
#         return f"{self.name}-{self.companyname}-{self.prn}-{self.address}-{self.username}-{self.password}"
    
#     class Meta:
#         verbose_name = "milk_Buyers"
#         verbose_name_plural = "milk_Buyers"
        
        
        

class MilkBuyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    companyname = models.CharField(max_length=100)
    prn = models.CharField(max_length=20, unique=True)
    address = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.companyname}"
    
    
    
# model for milk order

class MilkOrder(models.Model):
    buyer = models.ForeignKey('MilkBuyer', on_delete=models.CASCADE)  # Relation with MilkBuyer
    quantity = models.PositiveIntegerField()  # Quantity of milk requested
    request_date = models.DateTimeField(auto_now_add=True)  # Timestamp for the order

    def __str__(self):
        return f"{self.buyer.name} - {self.quantity} Liters"