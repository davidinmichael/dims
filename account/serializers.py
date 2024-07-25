from rest_framework import serializers
from rest_framework.response import Response
from .models import *

class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = ['id', 'platform', 'url']

class AccountSerializer(serializers.ModelSerializer):
    social_links = SocialLinkSerializer()
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
            "nationality",
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
            "nationality",
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
            "nationality",
            "password",
            "marital_status",
            "lecturer_rank",
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
            "nationality",
            "password",
            "marital_status",
            "is_admin_user"
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }
