# users/permissions.py
from rest_framework.permissions import BasePermission

class IsAdminOrSelf(BasePermission):
    """
    - Admins can view/list/delete any user.
    - Regular users can only view/update their own.
    """
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj == request.user
