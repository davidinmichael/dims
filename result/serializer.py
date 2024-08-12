from rest_framework import serializers
from .models import *




class CGPASerializer(serializers.ModelSerializer):

    class Meta:
        model = CGPA
        fields = "__all__"

        

class AddOutstanidngCourseSerializer(serializers.Serializer):
    course_id = serializers.IntegerField()
    student_id = serializers.IntegerField()