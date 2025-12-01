# Third-party app imports
from rest_framework import generics, permissions
from rest_framework import filters

# Local imports
from .models import Brand
from .serializers import BrandSerializer
from accounts.permissions import IsAdmin


class BrandListCreateView(generics.ListCreateAPIView):
    """List all brands (public) and create a new brand (admin only)."""
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'slug']

    def get_permissions(self):
        """Allow GET for everyone, restrict POST to admins."""
        if self.request.method == 'POST':
            return [IsAdmin()]
        return [permissions.AllowAny()]


class BrandDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve brand detail (public) and update/delete (admin only)."""
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def get_permissions(self):
        """Allow GET for everyone, restrict PATCH/DELETE to admins."""
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAdmin()]
        return [permissions.AllowAny()]
