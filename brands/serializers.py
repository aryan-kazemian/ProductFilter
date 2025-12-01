# Third-party app imports
from rest_framework import serializers

# Local imports
from .models import Brand


class BrandSerializer(serializers.ModelSerializer):
    """Serializer for brand model."""

    class Meta:
        model = Brand
        fields = ['id', 'name', 'slug']
