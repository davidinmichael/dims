from django.urls import path
from .views import *

urlpatterns = [
    path("", EventListCreatedView.as_view()),
    path("<int:pk>/", EventDetailView.as_view()),
]
