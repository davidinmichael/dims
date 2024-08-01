from django.urls import path
from .views import *

urlpatterns = [
    path("", CourseListCreate.as_view()),
    path('courses/', CourseView.as_view()),
    path("<int:pk>/", CourseDetail.as_view()),
    path("course_count/", CourseCounts.as_view()),
]