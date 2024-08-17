from django.urls import path
from .views import *

urlpatterns = [
    path("", ResultListCreate.as_view()),
    path("own_outstanding_courses/", UserOutstandingCourse.as_view()),
    path("add_outstanding_courses/", AddOutstandingCourse.as_view()),
]