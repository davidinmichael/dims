from rest_framework import serializers
from .models import Resource
from course.models import Courses
from course.serializers import CourseOutputSerializer
from account.models import Account


class ResourceSerializer(serializers.ModelSerializer):
    course = serializers.SlugRelatedField(slug_field="course_code", queryset=Courses.objects.all())

    class Meta:
        model = Resource
        fields = "__all__"
    

class ResourceOutputSerializer(serializers.ModelSerializer):
    course = CourseOutputSerializer(read_only=True)
    added_by = serializers.SlugRelatedField(slug_field="first_name", queryset=Account.objects.all())

    class Meta:
        model = Resource
        fields = "__all__"


class ResourceGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'resource', 'added_by']


class ResourceCourseSerializer(serializers.ModelSerializer):
    resources = ResourceGetSerializer(many=True, read_only=True)

    class Meta:
        model = Courses
        fields = [
            'id',
            'course_title',
            # 'course_unit',
            # 'course_code',
            # 'level',
            # 'semester',
            'resources',
        ]