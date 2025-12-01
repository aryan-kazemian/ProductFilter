# Core Django imports
from django.contrib import admin

# Third-party imports
from mptt.admin import DraggableMPTTAdmin

# Local imports
from .models import Category


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    """Admin for hierarchical categories with drag-and-drop ordering."""
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title', 'slug')
    list_display_links = ('indented_title',)
    search_fields = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}
