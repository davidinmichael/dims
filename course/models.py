from django.db import models
from course.choices import Status
# Create your models here.


class Courses(models.Model):
    Lecturer_name = models.CharField(max_length=255, null=True, blank=True)
    Lecturer_email = models.EmailField(max_length=255, null=True, blank=True)
    Lecture_day_and_time = models.DateTimeField(null=True, blank=True)

    course_status = models.CharField(max_length=255, choices=Status.choices, null=True, blank=True, default="Available")
    Course_title = models.CharField(max_length=255, null=True, blank=True)
    Course_unit = models.IntegerField(null=True, blank=True)
    Course_code = models.CharField(max_length=255, null=True, blank=True)
    Outstanding_courses = models.IntegerField(null=True, blank=True)
    
    semester = models.CharField(max_length=20, null=True, blank=True)
    current_cgpa = models.FloatField(null=True, blank=True)



    def __str__(self):
        return self.course_title