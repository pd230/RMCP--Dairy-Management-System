from django.contrib import admin

from .models import MilkOrder, MilkSeller, milk_pricing, MilkBuyer

@admin.register(MilkBuyer)
class MilkBuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_username', 'companyname', 'prn')

    def get_username(self, obj):
        return obj.user.username if obj.user else None  # Safely fetch username if user exists
    get_username.short_description = 'Username' 
    
# admin.site.register(milk_vendors)
admin.site.register(milk_pricing)

class MilkOrderAdmin(admin.ModelAdmin):
    list_display = ('buyer', 'quantity', 'request_date')
    list_filter = ('request_date',)
    search_fields = ('user__username', 'name', 'companyname')  # Corre # Updated search_fields for related User model

admin.site.register(MilkOrder, MilkOrderAdmin)
    
    
@admin.register(MilkSeller)
class MilkSellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_username', 'address', 'phone_no')

    def get_username(self, obj):
        return obj.user.username if obj.user else None  # Safely fetch username if user exists
    get_username.short_description = 'Username' 