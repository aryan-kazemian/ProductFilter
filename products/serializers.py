from rest_framework import serializers
from .models import Product
from categories.models import Category
from brands.models import Brand
from companies.models import Company
from attributes.models import Color, Gender, Age, Season, Country, Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'slug']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'slug']

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name', 'color', 'slug']

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ['id', 'name', 'slug']

class AgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Age
        fields = ['id', 'name', 'min_age', 'max_age', 'slug']

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ['id', 'name', 'slug']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'slug']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    company = CompanySerializer(read_only=True)
    color = ColorSerializer(read_only=True)
    gender = GenderSerializer(read_only=True)
    age = AgeSerializer(read_only=True)
    season = SeasonSerializer(read_only=True)
    country = CountrySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)


    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'rating', 'expire_date', 'category',
            'is_available', 'is_exciting', 'free_shipping', 'has_gift', 'is_budget_friendly',
            'price', 'brand', 'company', 'color', 'gender', 'age', 'season', 'country', 'tags',
            'created_at', 'updated_at'
        ]
