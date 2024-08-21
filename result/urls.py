from django.urls import path
from .views import *

urlpatterns = [
    path("", Result.as_view()),
    path("create_result/", ResultCreate.as_view()),
]