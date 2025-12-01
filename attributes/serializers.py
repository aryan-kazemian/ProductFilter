# Third-party app imports
from rest_framework import serializers

# Local imports
from .models import Country, Color, Gender, Age, Season, Tag


class CountrySerializer(serializers.ModelSerializer):
    """Serializer for country model."""
    class Meta:
        model = Country
        fields = ['id', 'name', 'slug']


class ColorSerializer(serializers.ModelSerializer):
    """Serializer for color model."""
    class Meta:
        model = Color
        fields = ['id', 'name', 'color', 'slug']


class GenderSerializer(serializers.ModelSerializer):
    """Serializer for gender model."""
    class Meta:
        model = Gender
        fields = ['id', 'name', 'slug']


class AgeSerializer(serializers.ModelSerializer):
    """Serializer for age range model."""
    class Meta:
        model = Age
        fields = ['id', 'name', 'min_age', 'max_age', 'slug']


class SeasonSerializer(serializers.ModelSerializer):
    """Serializer for season model."""
    class Meta:
        model = Season
        fields = ['id', 'name', 'slug']


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag model."""
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']
