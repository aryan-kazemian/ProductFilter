# Core Django imports
from django.db.models import Q

# Third-party app imports
from rest_framework import generics, permissions
from rest_framework import filters

# Local imports
from .models import Category
from .serializers import CategorySerializer
from accounts.permissions import IsAdmin


class CategoryListCreateView(generics.ListCreateAPIView):
    """List all categories (public) and create a new category (admin only)."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'slug']

    def get_permissions(self):
        """Allow GET for everyone, restrict POST to admins."""
        if self.request.method == 'POST':
            return [IsAdmin()]
        return [permissions.AllowAny()]


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve category detail (public) and update/delete (admin only)."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        """Allow GET for everyone, restrict PATCH/DELETE to admins."""
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAdmin()]
        return [permissions.AllowAny()]
