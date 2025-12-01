# Third-party app imports
from rest_framework import generics, permissions
from rest_framework import filters

# Local imports
from .models import Country, Color, Gender, Age, Season, Tag
from .serializers import (
    CountrySerializer, ColorSerializer, GenderSerializer,
    AgeSerializer, SeasonSerializer, TagSerializer
)
from accounts.permissions import IsAdmin


# Generic list/create view template
class AttributeListCreateView(generics.ListCreateAPIView):
    """Generic list/create view for attributes."""
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'slug']

    def get_permissions(self):
        """Allow GET for everyone, restrict POST to admins."""
        if self.request.method == 'POST':
            return [IsAdmin()]
        return [permissions.AllowAny()]


# Generic retrieve/update/delete view template
class AttributeDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Generic retrieve/update/delete view for attributes."""

    def get_permissions(self):
        """Allow GET for everyone, restrict PATCH/DELETE to admins."""
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAdmin()]
        return [permissions.AllowAny()]


# Country
class CountryListCreateView(AttributeListCreateView):
    """List all countries and create new country (admin only)."""
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDetailView(AttributeDetailView):
    """Retrieve, update or delete a country."""
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


# Color
class ColorListCreateView(AttributeListCreateView):
    """List all colors and create new color (admin only)."""
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class ColorDetailView(AttributeDetailView):
    """Retrieve, update or delete a color."""
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


# Gender
class GenderListCreateView(AttributeListCreateView):
    """List all genders and create new gender (admin only)."""
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer


class GenderDetailView(AttributeDetailView):
    """Retrieve, update or delete a gender."""
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer


# Age
class AgeListCreateView(AttributeListCreateView):
    """List all age ranges and create new age range (admin only)."""
    queryset = Age.objects.all()
    serializer_class = AgeSerializer


class AgeDetailView(AttributeDetailView):
    """Retrieve, update or delete an age range."""
    queryset = Age.objects.all()
    serializer_class = AgeSerializer


# Season
class SeasonListCreateView(AttributeListCreateView):
    """List all seasons and create new season (admin only)."""
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer


class SeasonDetailView(AttributeDetailView):
    """Retrieve, update or delete a season."""
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer


# Tag
class TagListCreateView(AttributeListCreateView):
    """List all tags and create new tag (admin only)."""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetailView(AttributeDetailView):
    """Retrieve, update or delete a tag."""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
