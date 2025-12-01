# Core Django imports
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Accounts (registration, JWT auth)
    path('api/accounts/', include('accounts.urls')),

    # Products
    path('api/products/', include('products.urls')),

    # Categories
    path('api/categories/', include('categories.urls')),

    # Brands
    path('api/brands/', include('brands.urls')),

    # Companies
    path('api/companies/', include('companies.urls')),

    # Attributes (countries, colors, gender, age, season, tags)
    path('api/attributes/', include('attributes.urls')),
]