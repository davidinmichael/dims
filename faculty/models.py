import datetime
from django.db import models
from account.models import Lecturer

# Create your models here.

class Faculty(models.Model):
    dept_name = models.CharField(max_length=255, blank=True, null=True)
    dept_description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='faculty_images/', blank=True, null= True,)
    
    first_name = models.CharField(blank=True, null=True, max_length=255)
    last_name = models.CharField(blank=True, null=True, max_length=255)
    middle_name = models.CharField(blank=True, null=True, max_length=255)
    rep_image = models.ImageField(upload_to= 'rep_images/', blank=True, null=True)
    rank = models.CharField(blank=True, null=True, max_length=25)
    academic_position = models.CharField(blank=True, null=True, max_length=20)
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.dept_name