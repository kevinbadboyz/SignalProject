from django.contrib import admin
from .models import Stock, Purchase

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('available_item', 'available_quantity')

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity')
