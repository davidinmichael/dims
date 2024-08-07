from django.contrib import admin
from .models import Courses, OutstandingCourses
# Register your models here.

admin.site.register([Courses, OutstandingCourses])