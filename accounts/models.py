# Core Django imports
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """Custom User model extending Django's AbstractUser with an optional role."""
    role = models.ForeignKey(
        'Role',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='users'
    )

    class Meta:
        """Meta information for the User model."""
        db_table = "User"
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        """Return the username of the user."""
        return self.username

class Role(models.Model):
    """Role model representing a user role in the system."""
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        """Meta information for the Role model."""
        db_table = "Role"
        verbose_name = "Role"
        verbose_name_plural = "Roles"

    def __str__(self):
        """Return the name of the role."""
        return self.name
