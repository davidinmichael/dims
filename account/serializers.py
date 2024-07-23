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


class StudentLoginSerializer(serializers.Serializer):
    matric_number = serializers.CharField()
    password = serializers.CharField(write_only=True)

# Student Signup Serializer
class StudentSignupSerializer(serializers.ModelSerializer):
    class Meta(AccountSerializer):
        model = Account
        fields = AccountSerializer.Meta.fields + [
            "matric_number",
            "level_year",
            "current_cgpa"
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

# Lecturer Login Serializer
class LecturerLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

# Lecturer Signup Serializer
class LecturerSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = AccountSerializer.Meta.fields + [
            "lecturer_title",
            "academic_role"
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

# Admin Login Serializer
class AdminLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

# Admin Signup Serializer
class AdminSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = AccountSerializer.Meta.fields + [
            "is_admin_user"
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }