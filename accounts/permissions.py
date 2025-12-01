# Third-party app imports
from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    """Permission class to allow access only to admin (staff) users."""

    def has_permission(self, request, view=None):
        """Check if the user is authenticated and a staff member."""
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)
