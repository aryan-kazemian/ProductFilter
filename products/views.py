from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter
from accounts.permissions import IsAdmin

class ProductListCreateView(generics.ListCreateAPIView):
    """List all products (public) and create product (admin only)."""
    queryset = Product.objects.select_related(
        'category', 'brand', 'company', 'color', 'gender', 'age', 'season', 'country'
    ).prefetch_related('tags').all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'rating', 'created_at']

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdmin()]
        return [permissions.AllowAny()]

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a product."""
    queryset = Product.objects.select_related(
        'category', 'brand', 'company', 'color', 'gender', 'age', 'season', 'country'
    ).prefetch_related('tags').all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAdmin()]
        return [permissions.AllowAny()]
