# Core Django imports
from django.contrib.auth import get_user_model

# Third-party app imports
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# Local imports
from accounts.models import Role

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):  
    """Serializer for registering new users."""

    class Meta:
        """Meta class for RegisterSerializer."""
        model = User
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        """Create a new User instance with hashed password."""
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def to_representation(self, instance):
        """Customize serialized representation including JWT tokens and user role."""
        refresh = RefreshToken.for_user(instance)
        data = {
            "user": {
                "id": instance.id,
                "username": instance.username,
                "role": instance.role.name if instance.role else None,
                "links": {
                    "self": f"/users/{instance.id}/",
                    "orders": f"/users/{instance.id}/orders/"
                }
            },
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }
        return data


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Custom serializer for obtaining JWT token pairs with user role."""

    @classmethod
    def get_token(cls, user):
        """Generate JWT token and include user's role."""
        token = super().get_token(user)
        token['role'] = user.role.name if user.role else None
        return token

    def to_representation(self, instance):
        """Standardize token response with nested user object and links."""
        data = super().to_representation(instance)
        user = self.user
        data = {
            "user": {
                "id": user.id,
                "username": user.username,
                "role": user.role.name if user.role else None,
                "links": {
                    "self": f"/users/{user.id}/",
                    "orders": f"/users/{user.id}/orders/"
                }
            },
            "access": data.get("access"),
            "refresh": data.get("refresh"),
        }
        return data
