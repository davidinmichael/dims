from django.urls import path
from .views import EventListView, EventDetailView, EventCreateView, EventUpdateView, EventDeleteView

urlpatterns = [
    path('events/', EventListView.as_view(), name='event_list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('events/create/', EventCreateView.as_view(), name='create_event'),
    path('events/<int:pk>/update/', EventUpdateView.as_view(), name='update_event'),
    path('events/<int:pk>/delete/', EventDeleteView.as_view(), name='delete_event'),
]
