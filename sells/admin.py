from django.contrib import admin
from .models import Customer,Sell,ItemSell,Order,ItemOrder
# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'address', 'phone')

class ItemSellAdmin(admin.TabularInline):
    model=ItemSell
    extra = 1

@admin.register(Sell)
class SellAdmin(admin.ModelAdmin):
    list_display = ('customer', 'created_by', 'creation_date')
    list_filter = ('customer', 'created_by', 'creation_date')
    search_fields = ('customer__name', 'created_by__username',)
    inlines = [ItemSellAdmin]

class ItemOrderAdmin(admin.TabularInline):
    model=ItemOrder
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'created_by', 'creation_date')
    list_filter = ('customer', 'created_by', 'creation_date')
    search_fields = ('customer__name', 'created_by__username', )
    inlines = [ItemOrderAdmin]
