from rest_framework import serializers
from .models import *


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = [
            "id",
            "dept_name",
            "dept_description",
            "image",
            "first_name",
            "last_name",
            "middle_name",
            "rep_image",
            "academic_position",
            "date_posted"
        ]