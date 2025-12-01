# Third-party app imports
from django.urls import path

# Local imports
from .views import CategoryListCreateView, CategoryDetailView


urlpatterns = [
    path('', CategoryListCreateView.as_view(), name='category_list'),
    path('<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
]
