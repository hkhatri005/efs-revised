from django.contrib import admin
from .models import Manager, Customer, Investment, Stock, User
from django.contrib.auth.admin import UserAdmin


class CustomerDetails(admin.ModelAdmin):

    list_display = ['user', 'name', 'cust_number', 'address', 'city', 'state', 'email', 'cell_phone']
    search_fields = ['name','cust_number']
    list_filter = ['name']


class InvestmentDetails(admin.ModelAdmin):

    list_display = ['customer', 'category', 'description', 'acquired_value', 'acquired_date', 'recent_value',
                    'recent_date']


class ManagerDetails(admin.ModelAdmin):
    list_display = ['user', 'name', 'address', 'city', 'state', 'email', 'cell_phone']


class StockDetails(admin.ModelAdmin):
    list_display = ['customer', 'symbol', 'name', 'shares', 'purchase_price', 'purchase_date']


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Manager, ManagerDetails)
admin.site.register(Customer, CustomerDetails)
admin.site.register(Investment, InvestmentDetails)
admin.site.register(Stock,StockDetails)
