from django.contrib import admin

from .models import milk_pricing, milk_vendors

admin.site.register(milk_vendors)
admin.site.register(milk_pricing)