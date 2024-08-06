from rest_framework import serializers
from .models import *


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = [
            "id",
            "name",
            "description",
            "image",
            "other_titles",
            "rep_name",
            "rep_role"
        ]