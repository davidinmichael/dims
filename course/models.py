from django.db import models
from course.choices import Status
# Create your models here.


class Courses(models.Model):
    lecturer_name = models.CharField(max_length=255, null=True, blank=True)
    lecturer_email = models.EmailField(max_length=255, null=True, blank=True)
    lecture_day_and_time = models.DateTimeField(null=True, blank=True)

    course_Status = models.CharField(max_length=255, choices=Status.choices, null=True, blank=True, default="Available")
    course_title = models.CharField(max_length=255, null=True, blank=True)
    course_unit = models.IntegerField(null=True, blank=True)
    course_code = models.CharField(max_length=255, null=True, blank=True)
    
    level = models.CharField(max_length=50, null=True, blank=True, default="level one")



    def __str__(self):
        return self.course_title