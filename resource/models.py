from django.db import models
from course.models import Courses
from account.models import Account


class Resource(models.Model):
    resource = models.FileField(upload_to="resources/")
    added_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
    course = models.ForeignKey(Courses, on_delete=models.SET_NULL, null=True, blank=True, related_name="resources")

    def __str__(self):
        return f"{self.course.course_title} | added by {self.added_by.first_name}"