from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'category', 'brand', 'company', 'price',
        'is_available', 'is_exciting', 'free_shipping', 'has_gift', 'is_budget_friendly',
        'created_at'
    )
    list_filter = (
        'is_available', 'is_exciting', 'free_shipping', 'has_gift', 'is_budget_friendly',
        'category', 'brand', 'company', 'color', 'gender', 'age', 'season', 'country', 'tags'
    )
