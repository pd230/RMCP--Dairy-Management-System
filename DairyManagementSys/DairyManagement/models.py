from django.db import models
from django.contrib.auth.models import User , auth

# Create your models here.
class Destination(models.Model): 
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    
