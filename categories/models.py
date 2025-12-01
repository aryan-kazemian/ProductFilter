# Core Django imports
from django.db import models
from django.utils.text import slugify

# Third-party app imports
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """Hierarchical product category model using MPTT with automatic unique slug generation."""
    name = models.CharField(max_length=255, unique=True)
    parent = TreeForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='children'
    )
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        db_table = 'Category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        """Generate unique slug on save based on the category name."""
        if not self.slug or (self.pk and Category.objects.get(pk=self.pk).name != self.name):
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Category.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        """Return the category name."""
        return self.name