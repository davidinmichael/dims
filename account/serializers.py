from rest_framework import serializers
from rest_framework.response import Response
from .models import *
from django.contrib.auth import authenticate

class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = ['id', 'platform', 'url']



class AccountSerializer(serializers.ModelSerializer):
    social_links = SocialLinkSerializer(required=False, many=True)

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
            "active_status",
            "profile_url",
            "social_links",
        ]

        extra_kwargs = {
            "id": {"read_only": True},
            "password": {"write_only": True},
        }
    
    def create(self, validated_data):
        social_links = validated_data.pop("social_links", [])
        user = Account.objects.create(**validated_data)
        for social_link in social_links:
            SocialLink.objects.create(user=user, **social_link)
        return user
    

# Student Serializer
class StudentSerializer(serializers.ModelSerializer):
    social_links = SocialLinkSerializer(required=False, many=True)

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
            "current_cgpa",
            "profile_url",
            "is_student",
            "social_links",
        ]

        extra_kwargs = {
            "password": {"write_only": True},
        }


# Lecturer Serializer
class LecturerSerializer(serializers.ModelSerializer):
    social_links = SocialLinkSerializer(required=False, many=True)

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
            "academic_role",
            "active_status",
            "is_lecturer",
            "profile_url",
            "social_links",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

# Admin Serializer
class AdminSerializer(serializers.ModelSerializer):
    social_links = SocialLinkSerializer(required=False, many=True)

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
            "is_admin_user",
            "profile_url",
            "social_links",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials")
    
    
class ForgotPasswordSerializer(serializers.Serializer):
    matric_number = serializers.CharField()
    email = serializers.EmailField() 