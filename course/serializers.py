from rest_framework import serializers
from .models import Courses, OutstandingCourses
from account.serializers import *


class CourseSerializer(serializers.ModelSerializer):
    # created_by = serializers.SlugRelatedField(
    #     slug_field="first_name", queryset=Account.objects.all(), required=False)
    # last_updated_by = serializers.SlugRelatedField(
    #     slug_field="first_name", queryset=Account.objects.all(), required=False)

    class Meta:
        model = Courses
        fields = [
            'id',
            'lecturer',
            'lecture_date',
            'lecture_time',
            'course_title',
            'course_unit',
            'course_code',
            'level',
            'semester',
            'created_by',
            'created_at',
            'last_updated_by',
            'last_updated',
        ]

class CourseOutputSerializer(serializers.ModelSerializer):
    lecturer = LecturerSerializer(required=False)
    created_by = serializers.SlugRelatedField(
        slug_field="first_name", queryset=Account.objects.all(), required=False)
    last_updated_by = serializers.SlugRelatedField(
        slug_field="first_name", queryset=Account.objects.all(), required=False)

    class Meta:
        model = Courses
        fields = [
            'id',
            'lecturer',
            'lecture_date',
            'lecture_time',
            'course_title',
            'course_unit',
            'course_code',
            'level',
            'semester',
            'created_by',
            'created_at',
            'last_updated_by',
            'last_updated',
        ]
    
    def validate(self, data):
        lecturer = data["lecturer"]
        if "admin" not in lecturer:
            return "Invalid data sent"
        return data
    
    def validate_level(self, value):
        if value == 1:
            return "Can't join event"
        


class OutstandingCourseSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, required=False)

    class Meta:
        model = OutstandingCourses
        fields = ["courses"]


class AddOutstanidngCourseSerializer(serializers.Serializer):
    course_id = serializers.IntegerField()
    student_id = serializers.IntegerField()
