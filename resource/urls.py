from django.urls import path
from .views import *


urlpatterns = [
    path("add-resource/", ResourceView.as_view()),
]
