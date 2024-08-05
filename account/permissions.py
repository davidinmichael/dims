from rest_framework.permissions import BasePermission, SAFE_METHODS

class CreateAccountPerm(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.method == "POST":
            return request.user.is_admin_user or request.user.is_lecturer
        return False
