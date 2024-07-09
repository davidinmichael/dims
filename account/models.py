from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext as _
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Please provide an email address")
        else:
            user = self.model( email=email, password=password, **extra_fields)
            password = user.set_password(password)
            user.save(using=self._db)
            return user
        
    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user

class Dataset(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    # Admin
    rank = models.CharField(max_length=50, null=True, blank=True)
    academic_position = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    state_of_origin = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to='users/', null=True, blank=True)
    active_status = models.BooleanField(default=True)
    marital_status = models.CharField(max_length=50, null=True, blank=True)
    social_handles = models.JSONField(null=True, blank=True)

    # Student
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    matric_number = models.CharField(max_length=50, unique=True, null=True, blank=True)
    level_year = models.IntegerField(null=True, blank=True)
    religion = models.CharField(max_length=50, null=True, blank=True)
    nationality = models.CharField(max_length=50, null=True, blank=True)

    # Courses Dataset
    number_of_courses = models.IntegerField(null=True, blank=True)
    current_semester_courses = models.JSONField(null=True, blank=True)  # Store course codes
    current_cgpa = models.FloatField(null=True, blank=True)
    outstanding_courses = models.JSONField(null=True, blank=True)  # Store course codes

    # Course table
    availability_status = models.BooleanField(default=True, null=True, blank=True)
    course_title = models.CharField(max_length=200, null=True, blank=True)
    course_unit = models.IntegerField(null=True, blank=True)
    lecture_day_time = models.DateTimeField(null=True, blank=True)
    course_code = models.CharField(max_length=50, null=True, blank=True)

    # Result Dataset
    examination_courses = models.JSONField(null=True, blank=True)  # Store course codes
    outstanding_courses = models.JSONField(null=True, blank=True)  # Store course codes
    year_semester = models.CharField(max_length=20, null=True, blank=True)
    search = models.CharField(max_length=100, null=True, blank=True)

    # Result table & Outstanding table
    lecturer_info = models.JSONField(null=True, blank=True)  # Store lecturer name & email
    score_grade = models.JSONField(null=True, blank=True)  # Store course code and score/grade

    # TLU, TCP & GPA
    tlu_present = models.FloatField(null=True, blank=True)
    tlu_previous = models.FloatField(null=True, blank=True)
    cumulative_gpa = models.FloatField(null=True, blank=True)

    # Dashboard
    current_level = models.IntegerField(null=True, blank=True)
    current_semester = models.IntegerField(null=True, blank=True)
    outstanding_courses = models.JSONField(null=True, blank=True)  # Store course codes
    courses = models.JSONField(null=True, blank=True)  # Store course titles and codes
    exams = models.JSONField(null=True, blank=True)  # Store exam details

    # Upcoming event
    event_title = models.CharField(max_length=200, null=True, blank=True)
    event_description = models.TextField(null=True, blank=True)
    event_date_time = models.DateTimeField(null=True, blank=True)

    # Contact page
    
    contact_phone_number = models.CharField(max_length=20, null=True, blank=True)
    contact_message = models.TextField(null=True, blank=True)

    # Address & WhatsApp
    office_school_address = models.CharField(max_length=200, null=True, blank=True)

    # Sign In (Usually handled by Django auth system)
    sign_in_email = models.EmailField(null=True, blank=True)
    sign_in_password = models.CharField(max_length=128, null=True, blank=True)
    sign_in_matric_number = models.CharField(max_length=50, unique=True, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        verbose_name=_('groups'),
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text=_('Specific permissions for this user.'),
        verbose_name=_('user permissions'),
    )

    USERNAME_FIELD = "username" # required field for login
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username

