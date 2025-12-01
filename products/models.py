# Core Django imports
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Local imports
from categories.models import Category
from brands.models import Brand
from companies.models import Company
from attributes.models import Color, Gender, Age, Season, Country, Tag


class Product(models.Model):
    """Main product model with full attributes and relations."""
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Product rating from 1 to 5"
    )
    expire_date = models.DateField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    is_available = models.BooleanField(default=True)
    is_exciting = models.BooleanField(default=False, help_text="Attractive or trending product")
    free_shipping = models.BooleanField(default=False)
    has_gift = models.BooleanField(default=False, help_text="Includes gift with product")
    is_budget_friendly = models.BooleanField(default=False, help_text="Cheap product")
    price = models.PositiveIntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, related_name='products')
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, related_name='products')
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, related_name='products')
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True, related_name='products')
    age = models.ForeignKey(Age, on_delete=models.SET_NULL, null=True, related_name='products')
    season = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True, related_name='products')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, related_name='products')
    tags = models.ManyToManyField(Tag, blank=True, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-created_at']

    def __str__(self):
        """Return product name."""
        return self.name
