from django.contrib import admin
from .models import Product, CartItem, PurchaseHistory


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'added_at')


@admin.register(PurchaseHistory)
class PurchaseHistoryAdmin(admin.ModelAdmin):
    list_display = ('purchase_date', 'total_amount', 'items_purchased')
    list_filter = ('purchase_date',)
    readonly_fields = ('purchase_date',)
