from django.urls import path
from .views import *

urlpatterns = [
    path("", CourseListCreate.as_view()),
    path("<int:pk>/", CourseDetail.as_view()),
]