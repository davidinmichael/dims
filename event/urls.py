from django.urls import path
from .views import *

urlpatterns = [
    path("", EventListCreatedView.as_view()),
    path("<int:pk>/", EventDetailView.as_view()),
    # path('events/create/', EventCreateView.as_view(), name='create_event'),
    # path('events/<int:pk>/update/', EventUpdateView.as_view(), name='update_event'),
    # path('events/<int:pk>/delete/', EventDeleteView.as_view(), name='delete_event'),
]
