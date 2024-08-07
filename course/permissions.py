from rest_framework import permissions
from account.models import *

class CourseWriteOrRead(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_admin_user or request.user.is_lecturer
