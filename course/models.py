from django.db import models
from core.choices import *
from course.choices import StudentLevel
# Create your models here.


class Courses(models.Model):
    lecturer_name = models.CharField(max_length=20, null=True, blank=True)
    lecturer_email = models.EmailField(max_length=20, null=True, blank=True)
    lecture_date = models.DateField(null=True, blank=True) # "yyyy-mm-dd"
    lecture_time = models.TimeField(null=True, blank=True) # "HH:MM"

    lecturer_availability = models.CharField(max_length=15, choices=Availability.choices, null=True, blank=True, default=Availability.AVAILABLE)
    course_title = models.CharField(max_length=50, null=True, blank=True)
    course_unit = models.CharField(max_length=20, null=True, blank=True)
    course_code = models.CharField(max_length=20, null=True, blank=True)
    
    level = models.CharField(choices=StudentLevel.choices, max_length=15, null=True, blank=True, default=StudentLevel.LEVEL_ONE)



    def __str__(self):
        return self.course_title