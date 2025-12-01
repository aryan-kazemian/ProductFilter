# Third-party app imports
from rest_framework import generics, permissions
from rest_framework import filters

# Local imports
from .models import Company
from .serializers import CompanySerializer
from accounts.permissions import IsAdmin


class CompanyListCreateView(generics.ListCreateAPIView):
    """List all companies (public) and create new company (admin only)."""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'slug']

    def get_permissions(self):
        """Allow GET for everyone, restrict POST to admins."""
        if self.request.method == 'POST':
            return [IsAdmin()]
        return [permissions.AllowAny()]


class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve company detail (public) and update/delete (admin only)."""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_permissions(self):
        """Allow GET for everyone, restrict PATCH/DELETE to admins."""
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAdmin()]
        return [permissions.AllowAny()]
