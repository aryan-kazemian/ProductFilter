# Core Django imports
from django.urls import path

# Third-party app imports
from rest_framework_simplejwt.views import TokenRefreshView

# Local imports
from .views import RegisterView, CustomTokenObtainPairView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),

    # JWT Token
    path('tokens/', CustomTokenObtainPairView.as_view(), name='token_create'),
    path('tokens/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
