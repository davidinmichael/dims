from django.db import models
from account.models import Lecturer

# Create your models here.

class Faculty(models.Model):
    dept_name = models.CharField(max_length=255, blank=True, null=True)
    info_description = models.TextField(blank=True, null=True)
    images = models.ImageField(upload_to='faculty_images/', blank=True, null= True,)
    
    reps_name = models.CharField(blank=True, null=True, max_length=255)
    reps_role = models.CharField(blank=True, null=True, max_length=20)