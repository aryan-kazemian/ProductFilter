# Core Django imports
from django.db import models
from django.utils.text import slugify


class Brand(models.Model):
    """Brand model with automatic unique slug generation."""
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        db_table = 'Brand'
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        ordering = ['name']

    def save(self, *args, **kwargs):
        """Generate unique slug on save based on the brand name."""
        if not self.slug or (self.pk and Brand.objects.get(pk=self.pk).name != self.name):
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Brand.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        """Return the brand name."""
        return self.name
