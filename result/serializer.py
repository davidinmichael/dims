from rest_framework import serializers
from .models import *



class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = [
            "id",
            "lecturer",
            "course_title",
            "course_unit",
            "course_code",
            "score"
        ]



class OutstandingCourseSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, required=False)

    class Meta:
        model = OutstandingCourse
        fields = ["courses"]



class CGPASerializer(serializers.ModelSerializer):

    class Meta:
        model = CGPA
        fields = "__all__"

        

class AddOutstanidngCourseSerializer(serializers.Serializer):
    course_id = serializers.IntegerField()
    student_id = serializers.IntegerField()