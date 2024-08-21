from rest_framework import serializers

from course.models import OutstandingCourses
from course.serializers import CourseSerializer
from .models import *
from account.models import Student



class ResultSerializer(serializers.ModelSerializer):
    student = serializers.SlugRelatedField(
        queryset=Student.objects.all(),
        slug_field='matric_number',
    )
    course = serializers.SlugRelatedField(
        queryset=Courses.objects.all(),
        slug_field='course_code',
    )

    class Meta:
        model = Result
        fields = "__all__"
