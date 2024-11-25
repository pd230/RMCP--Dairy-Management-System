from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User , auth
from accounts.models import milk_pricing

# Create your models here.
class MilkCollection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='milk_collections')  # Link to User
    grade = models.ForeignKey(milk_pricing, on_delete=models.CASCADE, related_name='collections')  # Link to Milk Pricing
    liters_collected = models.DecimalField(max_digits=5, decimal_places=2)  # Quantity in liters
    collection_date = models.DateField(auto_now_add=True)  # Date of collection
    total_amount = models.DecimalField(max_digits=8, decimal_places=2, editable=False)  # Automatically calculated
    
    def save(self, *args, **kwargs):
        # Automatically calculate total amount before saving
        self.total_amount = Decimal(self.grade.price_per_liter) * Decimal(self.liters_collected)
        super().save(*args, **kwargs)  # Call the parent class save method
    
    def __str__(self):
        return f"{self.user.username} - {self.grade.quality} {self.grade.grade} - {self.liters_collected}-{self.collection_date}-{self.total_amount}"

    class Meta:
        verbose_name = "Milk Collection"
        verbose_name_plural = "Milk Collections"
    
