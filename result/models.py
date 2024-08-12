from django.db import models
from account.models import Lecturer, Student
from course.models import Courses
from core.choices import *
# Create your models here.





class Result(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="results")
    course = models.ForeignKey(Courses, related_name="results")
    score = models.PositiveIntegerField(null=True, blank=True)
    def __str__(self):
        return f"{self.student} - {self.course}"





