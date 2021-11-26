# main_app/permissions

from rest_framework import permissions


class IsSalonOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow read-only permissions for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # write permissions are only allowed to the owners of a salon
        return obj.owner == request.user
