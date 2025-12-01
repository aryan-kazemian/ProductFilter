# Core Django imports
from django.db import models
from django.utils.text import slugify


class Company(models.Model):
    """Company model with automatic unique slug generation."""
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        db_table = 'Company'
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ['name']

    def save(self, *args, **kwargs):
        """Generate unique slug on save based on the company name."""
        if not self.slug or (self.pk and Company.objects.get(pk=self.pk).name != self.name):
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Company.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        """Return the company name."""
        return self.name
