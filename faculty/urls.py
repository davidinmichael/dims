from django.urls import path
from .views import *


urlpatterns = [
    path("", FacultyView.as_view()),
    path("<int:pk>/", FacultyDetail.as_view())
]