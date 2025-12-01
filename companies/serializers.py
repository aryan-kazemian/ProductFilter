# Third-party app imports
from rest_framework import serializers

# Local imports
from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    """Serializer for company model."""

    class Meta:
        model = Company
        fields = ['id', 'name', 'slug']
