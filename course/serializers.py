from rest_framework import serializers
from .models import Courses
from account.serializers import *

class CourseSerializer(serializers.ModelSerializer):
    lecturer = LecturerSerializer(required=False)
    last_updated_by = serializers.SlugRelatedField(slug_field="first_name", queryset=Account.objects.all(), required=False)
    
    class Meta:
        model = Courses
        fields = [
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

                
        