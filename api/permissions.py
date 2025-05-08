from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrCreateOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method == "POST":
            return True
        return request.user and request.user.is_staff


class IsAdminOrGetOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        return request.user and request.user.is_staff
