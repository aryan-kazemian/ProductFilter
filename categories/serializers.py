# Third-party app imports
from rest_framework import serializers

# Local imports
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for category model with hierarchical structure."""

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'parent']
