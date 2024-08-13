from django.urls import path
from .views import *


urlpatterns = [
    path("add-resource/", ResourceView.as_view()),
    path('courses-with-resources/', CourseResourceView.as_view()),
]
