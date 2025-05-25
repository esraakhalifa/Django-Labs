# permissions.py

from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Safe methods are allowed for everyone (if authenticated)
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only for the post owner
        return obj.author == request.user

    def has_permission(self, request, view):
        # User must be authenticated for any action
        return request.user and request.user.is_authenticated
