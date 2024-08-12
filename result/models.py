from django.db import models
from account.models import Lecturer, Student
from course.models import Course
from core.choices import *
# Create your models here.





class Result(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="results")
    course = models.ManyToManyField(Course, related_name="results")
    year = models.IntegerField(choices=StudentLevel.choices, null=True, blank=True, default=StudentLevel.LEVEL_ONE)
    semester = models.IntegerField(choices=SchoolSemester.choices, null=True, blank=True, default=SchoolSemester.FIRST_SEMESTER)

    def __str__(self):
        return f"{self.student} - {self.course} - {self.grade}"




class CGPA(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="cgpa")
    current_gpa = models.DecimalField(max_digits=4, decimal_places=2)
    cumulative_gpa = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.student} - Current GPA: {self.current_gpa}, Cumulative GPA: {self.cumulative_gpa}"
