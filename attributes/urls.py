# Third-party app imports
from django.urls import path

# Local imports
from .views import (
    CountryListCreateView, CountryDetailView,
    ColorListCreateView, ColorDetailView,
    GenderListCreateView, GenderDetailView,
    AgeListCreateView, AgeDetailView,
    SeasonListCreateView, SeasonDetailView,
    TagListCreateView, TagDetailView
)

urlpatterns = [
    # Country
    path('countries/', CountryListCreateView.as_view(), name='country_list'),
    path('countries/<int:pk>/', CountryDetailView.as_view(), name='country_detail'),

    # Color
    path('colors/', ColorListCreateView.as_view(), name='color_list'),
    path('colors/<int:pk>/', ColorDetailView.as_view(), name='color_detail'),

    # Gender
    path('genders/', GenderListCreateView.as_view(), name='gender_list'),
    path('genders/<int:pk>/', GenderDetailView.as_view(), name='gender_detail'),

    # Age
    path('ages/', AgeListCreateView.as_view(), name='age_list'),
    path('ages/<int:pk>/', AgeDetailView.as_view(), name='age_detail'),

    # Season
    path('seasons/', SeasonListCreateView.as_view(), name='season_list'),
    path('seasons/<int:pk>/', SeasonDetailView.as_view(), name='season_detail'),

    # Tag
    path('tags/', TagListCreateView.as_view(), name='tag_list'),
    path('tags/<int:pk>/', TagDetailView.as_view(), name='tag_detail'),
]
