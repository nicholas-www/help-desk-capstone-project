from rest_framework import permissions


class IsAgent(permissions.BasePermission):
    """
    Allow access to users with is_agent=True
    """

    def has_permission(self, request, view):
        user = request.user if request.user else None
        return user.is_authenticated and user.is_agent

