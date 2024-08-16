from rest_framework import serializers
from .models import *



class ResultSerializer(serializers.ModelSerializer):
    matric_number = serializers.SlugRelatedField(
        source='student',
        slug_field='matric_number',
    )

    class Meta:
        model = Result
        fields = "__all__" 


class ResultOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ["student_id", "course_id", "grade", "semester"]