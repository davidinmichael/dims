from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from rest_framework.response import Response

from .choices import *
from core.choices import *


class AccountManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            return Response({"message": "Users must have an email address."})
        email = self.normalize_email(email)

        groups = extra_fields.pop('groups', None)
        user_permissions = extra_fields.pop('user_permissions', None)

        user = self.model(email=email, **extra_fields)
        if password is not None:
            user.set_password(password)
        user.save(using=self._db)

        if groups:
            user.groups.set(groups)
        if user_permissions:
            user.user_permissions.set(user_permissions)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractUser):
    # Common Fields
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)  # "YYYY-MM-DD"
    gender = models.CharField(
        max_length=10, choices=Gender.choices, null=True, blank=True, default="")
    religion = models.CharField(
        max_length=20, null=True, blank=True, default="")
    phone_number = models.CharField(
        max_length=20, null=True, blank=True, default="")
    state = models.CharField(max_length=20, blank=True, null=True, default="")
    profile_picture = models.ImageField(
        upload_to="profile_images/", default="profile_images/default-profile-image.png", blank=True, null=True)
    nationality = models.CharField(
        max_length=20, blank=True, null=True, default="Nigeria")
    marital_status = models.CharField(
        max_length=20, null=False, blank=True, default="")
    profile_url = models.CharField(max_length=30, null=True, blank=True)
    otp_token = models.CharField(max_length=5, null=True, blank=True)

    # Admin Fields
    is_admin_user = models.BooleanField(default=True)
    is_student = models.BooleanField(default=False)
    is_lecturer = models.BooleanField(default=False)

    username = models.CharField(max_length=20, null=True, blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = AccountManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.email}"

    def user_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def is_admin_or_lecturer(self):
        return any([self.is_admin_user, self.is_lecturer])


class Student(models.Model):
    user = models.OneToOneField(
        Account, on_delete=models.CASCADE)
    matric_number = models.CharField(max_length=20, null=True, blank=True)
    level_year = models.IntegerField(
        choices=StudentLevel.choices, null=True, blank=True)
    current_semester = models.IntegerField(
        choices=SchoolSemester.choices, null=True, blank=True, default=SchoolSemester.FIRST_SEMESTER)
    current_cgpa = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} | {self.user.is_student}"


class Lecturer(models.Model):
    user = models.OneToOneField(
        Account, on_delete=models.CASCADE)
    lecturer_rank = models.CharField(max_length=20, null=True, blank=True)
    academic_role = models.CharField(max_length=20, null=True, blank=True)
    lecturer_availability = models.CharField(
        max_length=20, choices=Availability.choices, default=Availability.AVAILABLE, null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} | {self.user.is_lecturer}"

class SocialLink(models.Model):
    user = models.ForeignKey(
        Account, related_name='social_links', on_delete=models.CASCADE)
    platform = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return f'{self.platform}: {self.url}'
