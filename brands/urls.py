# Third-party app imports
from django.urls import path

# Local imports
from .views import BrandListCreateView, BrandDetailView


urlpatterns = [
    path('', BrandListCreateView.as_view(), name='brand_list'),
    path('<int:pk>/', BrandDetailView.as_view(), name='brand_detail'),
]
