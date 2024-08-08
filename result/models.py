from django.db import models
from account.models import Lecturer, Student
from core.choices import *
# Create your models here.



class Course(models.Model):
    course_title = models.CharField(max_length=50, null=True, blank=True)
    course_unit = models.CharField(max_length=20, null=True, blank=True)
    course_code = models.CharField(max_length=20, null=True, blank=True, unique=True)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, related_name="courses")

    def __str__(self):
        return f"{self.code} - {self.title}"



class Result(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="results")
    course = models.ManyToManyField(Course, related_name="results")
    score = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.CharField(max_length=2)
    year = models.IntegerField(choices=StudentLevel.choices, null=True, blank=True, default=StudentLevel.LEVEL_ONE)
    semester = models.IntegerField(choices=SchoolSemester.choices, null=True, blank=True, default=SchoolSemester.FIRST_SEMESTER)

    def __str__(self):
        return f"{self.student} - {self.course} - {self.grade}"



class OutstandingCourse(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, null=True, blank=True)
    course = models.ManyToManyField(Course, related_name="outstanding_courses")


    def __str__(self):
        return f"{self.student} - {self.course}"

class CGPA(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="cgpa")
    current_gpa = models.DecimalField(max_digits=4, decimal_places=2)
    cumulative_gpa = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.student} - Current GPA: {self.current_gpa}, Cumulative GPA: {self.cumulative_gpa}"
