from rest_framework import serializers
from rest_framework.response import Response
from .models import *
from course.models import OutstandingCourses


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = ['id', 'platform', 'url']


class AccountSerializer(serializers.ModelSerializer):
    social_links = SocialLinkSerializer(required=False, many=True)

    class Meta:
        model = Account
        fields = [
            "id",
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
            "profile_url",
            "is_admin_user",
            "is_student",
            "is_lecturer",
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
    
    def update(self, instance, validated_data):
        restricted_fields = [
            'email',
            'state',
            'gender',
            'date_of_birth',
            'nationality'
        ]
        
        # Check if any restricted field is being updated
        for field in restricted_fields:
            if field in validated_data:
                raise serializers.ValidationError(f"{field.replace('_', ' ').title()} cannot be updated.")

        # Update other fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
    


# Student Serializer
class StudentSerializer(serializers.ModelSerializer):
    user = AccountSerializer()
    social_links = SocialLinkSerializer(required=False, many=True)

    class Meta:
        model = Student
        fields = [
            "id",
            "user",
            "matric_number",
            "level_year",
            "current_semester",
            "current_cgpa",
            "social_links",
        ]
    
    def create(self, validated_data):
        social_links = validated_data.pop("social_links", [])
        user_data = validated_data.pop("user")
        user = Account.objects.create(is_student=True, **user_data)
        student = Student.objects.create(user=user, **validated_data)
        user.is_student = True
        user.save()
        OutstandingCourses.objects.create(user=student)

        for social_link in social_links:
            SocialLink.objects.create(user=user, **social_link)
        return student


# Lecturer Serializer
class LecturerSerializer(serializers.ModelSerializer):
    user = AccountSerializer()
    social_links = SocialLinkSerializer(required=False, many=True)

    class Meta:
        model = Lecturer
        fields = [
            "id",
            "user",
            "lecturer_rank",
            "academic_role",
            "lecturer_availability",
            "social_links",
        ]

    def create(self, validated_data):
        social_links = validated_data.pop("social_links", [])
        user_data = validated_data.pop("user")
        user = Account.objects.create(**user_data)
        lecturer = Lecturer.objects.create(user=user, **validated_data)
        user.is_lecturer = True
        user.save()

        for social_link in social_links:
            SocialLink.objects.create(user=user, **social_link)
        return lecturer

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
    password = serializers.CharField()


class SetNewPasswordSerializer(serializers.Serializer):
    otp_token = serializers.CharField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("Passwords do not match")
        return data