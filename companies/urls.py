# Third-party app imports
from django.urls import path

# Local imports
from .views import CompanyListCreateView, CompanyDetailView


urlpatterns = [
    path('', CompanyListCreateView.as_view(), name='company_list'),
    path('<int:pk>/', CompanyDetailView.as_view(), name='company_detail'),
]
