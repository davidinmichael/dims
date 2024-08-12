from django.urls import path
from .views import *

urlpatterns = [
    path("", ResultListCreate.as_view()),
]