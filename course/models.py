from django.db import models
from django.utils import timezone

from account.models import Account, Lecturer, Student
from core.choices import *


class Courses(models.Model):
    lecturer = models.ForeignKey(Lecturer, related_name="lecturer_courses", on_delete=models.SET_NULL, null=True, blank=True)

    lecture_date = models.DateField(null=True, blank=True) # "yyyy-mm-dd"
    lecture_time = models.TimeField(null=True, blank=True) # "HH:MM"

    course_title = models.CharField(max_length=50, null=True, blank=True)
    course_unit = models.CharField(max_length=20, null=True, blank=True)
    course_code = models.CharField(max_length=20, null=True, blank=True)
    level = models.IntegerField(choices=StudentLevel.choices, null=True, blank=True, default=StudentLevel.LEVEL_ONE)
    semester = models.IntegerField(choices=SchoolSemester.choices, null=True, blank=True, default=SchoolSemester.FIRST_SEMESTER)

    created_by = models.ForeignKey(Account, related_name="created_by_user", on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_by = models.ForeignKey(Account, related_name="updated_by_user", on_delete=models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_title


class OutstandingCourses(models.Model):
    user = models.OneToOneField(Student, on_delete=models.CASCADE, null=True, blank=True)
    courses = models.ManyToManyField(Courses, related_name="outstanding_courses")

    def __str__(self):
        return str(self.user.matric_number)
    
    def count_courses(self):
        return self.courses.count()