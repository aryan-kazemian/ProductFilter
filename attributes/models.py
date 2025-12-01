# Core Django imports
from django.db import models
from django.utils.text import slugify


class Country(models.Model):
    """Country model with unique slug."""
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        db_table = 'Country'
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        ordering = ['name']

    def save(self, *args, **kwargs):
        """Generate unique slug from country name."""
        if not self.slug or (self.pk and Country.objects.get(pk=self.pk).name != self.name):
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Country.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        """Return country name."""
        return self.name


class Color(models.Model):
    """Color model with name, hex code, and slug."""
    name = models.CharField(max_length=100, unique=True)
    color = models.CharField(max_length=7)  # Hex code like #FF0000
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        db_table = 'Color'
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'
        ordering = ['name']

    def save(self, *args, **kwargs):
        """Generate unique slug from color name."""
        if not self.slug or (self.pk and Color.objects.get(pk=self.pk).name != self.name):
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Color.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        """Return color name."""
        return self.name


class Gender(models.Model):
    """Gender model with fixed choices."""
    MALE = 'male'
    FEMALE = 'female'
    BOTH = 'both'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (BOTH, 'Both'),
    ]

    name = models.CharField(max_length=10, choices=GENDER_CHOICES, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        db_table = 'Gender'
        verbose_name = 'Gender'
        verbose_name_plural = 'Genders'
        ordering = ['name']

    def save(self, *args, **kwargs):
        """Generate slug from gender name."""
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        """Return gender name."""
        return self.name


class Age(models.Model):
    """Age range model with min, max and slug."""
    name = models.CharField(max_length=255)
    min_age = models.PositiveIntegerField()
    max_age = models.PositiveIntegerField()
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        db_table = 'Age'
        verbose_name = 'Age Range'
        verbose_name_plural = 'Age Ranges'
        ordering = ['min_age']

    def save(self, *args, **kwargs):
        """Generate slug from name."""
        if not self.slug or (self.pk and Age.objects.get(pk=self.pk).name != self.name):
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Age.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        """Return age range name."""
        return self.name


class Season(models.Model):
    """Season model with slug."""
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    class Meta:
        db_table = 'Season'
        verbose_name = 'Season'
        verbose_name_plural = 'Seasons'
        ordering = ['name']

    def save(self, *args, **kwargs):
        """Generate slug from name."""
        if not self.slug or (self.pk and Season.objects.get(pk=self.pk).name != self.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        """Return season name."""
        return self.name


class Tag(models.Model):
    """Tag model with slug."""
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        db_table = 'Tag'
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['name']

    def save(self, *args, **kwargs):
        """Generate slug from name."""
        if not self.slug or (self.pk and Tag.objects.get(pk=self.pk).name != self.name):
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Tag.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        """Return tag name."""
        return self.name
