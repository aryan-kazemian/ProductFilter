# Core Django imports
from django.contrib.auth import get_user_model

# Third-party app imports
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView

# Local imports
from .serializers import RegisterSerializer, CustomTokenObtainPairSerializer

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    """Handle user registration."""
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    """Obtain JWT access and refresh tokens for a user."""
    serializer_class = CustomTokenObtainPairSerializer
