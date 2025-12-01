# Third-party imports
from django_filters import rest_framework as filters

# Local imports
from .models import Product


class ProductFilter(filters.FilterSet):
    """Filter for all product fields."""
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    category = filters.NumberFilter(field_name="category__id")
    brand = filters.NumberFilter(field_name="brand__id")
    company = filters.NumberFilter(field_name="company__id")
    color = filters.NumberFilter(field_name="color__id")
    gender = filters.NumberFilter(field_name="gender__id")
    age = filters.NumberFilter(field_name="age__id")
    season = filters.NumberFilter(field_name="season__id")
    country = filters.NumberFilter(field_name="country__id")
    tags = filters.BaseInFilter(field_name="tags__id", lookup_expr='in')
    is_available = filters.BooleanFilter(field_name="is_available")
    is_exciting = filters.BooleanFilter(field_name="is_exciting")
    free_shipping = filters.BooleanFilter(field_name="free_shipping")
    has_gift = filters.BooleanFilter(field_name="has_gift")
    is_budget_friendly = filters.BooleanFilter(field_name="is_budget_friendly")
    rating = filters.NumberFilter(field_name="rating")

    class Meta:
        model = Product
        fields = [
            'category', 'brand', 'company', 'color', 'gender', 'age', 'season', 'country', 'tags',
            'is_available', 'is_exciting', 'free_shipping', 'has_gift', 'is_budget_friendly', 'rating',
            'min_price', 'max_price'
        ]
