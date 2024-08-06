from django.db import models
from account.models import Lecturer

# Create your models here.

class Faculty(models.Model):
    dept_name = models.CharField(max_length=255, blank=True, null=True)
    info_description = models.TextField(blank=True, null=True)
    images = models.ImageField(upload_to='faculty_images/', blank=True, null= True,)
    other_titles = models.CharField(blank=True, null=True, max_length=50)
    
    reps_name = models.OneToOneField(
        Lecturer, on_delete=models.CASCADE)
    reps_degree = models.CharField(max_length=20, null=True, blank=True)