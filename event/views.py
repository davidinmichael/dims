from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework import serializers
from .models import Event
import json

# Serializer for Event model
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

# Custom permission class
class IsCustomAdminUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_admin_user)

class EventListView(APIView):
    """
    API view to retrieve a list of events specific to the logged-in user.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        events = Event.objects.filter(user=request.user)
        serializer = EventSerializer(events, many=True)
        return JsonResponse(serializer.data, safe=False)


class EventDetailView(APIView):
    """
    API view to retrieve details of a specific event.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        event = get_object_or_404(Event, pk=pk, user=request.user)
        serializer = EventSerializer(event)
        return JsonResponse(serializer.data, safe=False)

class EventCreateView(LoginRequiredMixin, APIView):
    """
    API view to create a new event (requires login).
    """
    permission_classes = [IsAuthenticated, IsCustomAdminUser]

    def post(self, request):
        data = json.loads(request.body)
        data['user'] = request.user.id
        serializer = EventSerializer(data=data)
        if serializer.is_valid():
            event = serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class EventUpdateView(LoginRequiredMixin, APIView):
    """
    API view to update an existing event (requires login).
    """
    permission_classes = [IsAuthenticated, IsCustomAdminUser]

    def put(self, request, pk):
        event = get_object_or_404(Event, pk=pk, user=request.user)
        data = json.loads(request.body)
        serializer = EventSerializer(event, data=data, partial=True)
        if serializer.is_valid():
            event = serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


class EventDeleteView(LoginRequiredMixin, APIView):
    """
    API view to delete an existing event (requires login).
    """
    permission_classes = [IsAuthenticated, IsCustomAdminUser]

    def delete(self, request, pk):
        event = get_object_or_404(Event, pk=pk, user=request.user)
        event.delete()
        return JsonResponse({'message': 'Event deleted successfully'})
