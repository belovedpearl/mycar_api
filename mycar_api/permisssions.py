from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Grant all users read-only access
    Allows owners full access for unsafe methods

    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user