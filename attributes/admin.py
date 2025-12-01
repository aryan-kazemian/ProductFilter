from django.contrib import admin
from .models import Country, Color, Gender, Age, Season, Tag


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    """Admin for Country."""
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}
    ordering = ('name',)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    """Admin for Color."""
    list_display = ('name', 'color', 'slug')
    search_fields = ('name', 'color')
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ('color',)
    ordering = ('name',)


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    """Admin for Gender."""
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}
    ordering = ('name',)


@admin.register(Age)
class AgeAdmin(admin.ModelAdmin):
    """Admin for Age range."""
    list_display = ('name', 'min_age', 'max_age', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}
    ordering = ('min_age',)


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    """Admin for Season."""
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}
    ordering = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Admin for Tag."""
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}
    ordering = ('name',)
