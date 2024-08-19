from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied



class IsLecturerOfCourse(BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.is_lecturer or obj.is_admin_user != request.user:
            raise PermissionDenied(detail="You are not allowed")
        return True
