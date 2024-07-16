from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from .models import Event
import json

class EventListView(APIView):
    """
    API view to retrieve a list of all events.
    """
    def get(self, request):
        event = Event.objects.all()
        event_list = list(event.values())
        return JsonResponse({'event': event_list})

class EventDetailView(APIView):
    """
    API view to retrieve details of a specific event.
    """
    def get(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        event_data = {
            'title': event.title,
            'description': event.description,
            'image': event.image.url if event.image else None,  # Handle case where image is null
            'date': event.date,
            'location': event.location,
        }
        return JsonResponse({'event': event_data})

class EventCreateView(LoginRequiredMixin, APIView):
    """
    API view to create a new event (requires login).
    """
    permission_classes = [IsAdminUser]

    def post(self, request):
        data = json.loads(request.body)
        event = Event.objects.create(
            title=data['title'],
            description=data['description'],
            date=data['date'],
            location=data['location'],
        )
        return JsonResponse({'message': 'Event created successfully', 'event': event.id})

class EventUpdateView(LoginRequiredMixin, APIView):
    """
    API view to update an existing event (requires login).
    """
    permission_classes = [IsAdminUser]

    def put(self, request, pk):
        # Assuming CSRF protection is handled by Django middleware
        event = get_object_or_404(Event, pk=pk)
        data = json.loads(request.body)
        event.title = data.get('title', event.title)
        event.description = data.get('description', event.description)
        event.date = data.get('date', event.date)
        event.location = data.get('location', event.location)
        event.save()
        return JsonResponse({'message': 'Event updated successfully'})

class EventDeleteView(LoginRequiredMixin, APIView):
    """
    API view to delete an existing event (requires login).
    """
    permission_classes = [IsAdminUser]

    def delete(self, request, pk):
        # Assuming CSRF protection is handled by Django middleware
        event = get_object_or_404(Event, pk=pk)
        event.delete()
        return JsonResponse({'message': 'Event deleted successfully'})
