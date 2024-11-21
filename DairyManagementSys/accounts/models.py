from django.db import models
from django.contrib.auth.models import User , auth

# Create your models here.
class milk_vendors(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=10, unique=True)
    join_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.user.objects
    
    