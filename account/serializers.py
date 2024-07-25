from rest_framework import serializers
from rest_framework.response import Response
from .models import *


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "gender",
            "religion",
            "phone_number",
            "state",
            "profile_picture",
            "country",
            "is_admin_user",
            "password",
            "marital_status",
            "matric_number",
            "level_year",
            "current_cgpa",
            "lecturer_title",
            "academic_role",
            "active_status"
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "password": {"write_only": True},
        }

# Student Serializer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "gender",
            "religion",
            "phone_number",
            "state",
            "profile_picture",
            "country",
            "password",
            "marital_status",
            "matric_number",
            "level_year",
            "current_cgpa"
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }


# Lecturer Serializer
class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "gender",
            "religion",
            "phone_number",
            "state",
            "profile_picture",
            "country",
            "password",
            "marital_status",
            "lecturer_title",
            "academic_role"
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

# Admin Serializer
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = AccountSerializer.Meta.fields + [
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "gender",
            "religion",
            "phone_number",
            "state",
            "profile_picture",
            "country",
            "password",
            "marital_status",
            "is_admin_user"
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }
