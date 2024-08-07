from functools import partial
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import *
from .models import Event

class EventListCreatedView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        events = Event.objects.all().order_by("-created_at")
        if events:
            serializer = EventSerializer(events, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        return Response({"message": "Events will apear here."}, status.HTTP_200_OK)
    
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save(created_by=request.user)
            return Response({"message": "Event Created."}, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class EventDetailView(APIView):
    """
    API view to retrieve details of a specific event.
    """

    def get(self, request, pk):
        try:
            event = Event.objects.get(id=pk)
        except Event.DoesNotExist:
            return Response({"message": "No event found"}, status.HTTP_404_NOT_FOUND)
        serializer = EventSerializer(event)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def put(self, request, pk):
        try:
            event = Event.objects.get(id=pk)
        except Event.DoesNotExist:
            return Response({"message": "No event found"}, status.HTTP_404_NOT_FOUND)
        serializer = EventSerializer(event, data=request.data, partial = True)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response({"message": "Event Updated"}, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            event = Event.objects.get(id=pk)
        except Event.DoesNotExist:
            return Response({"message": "No event found"}, status.HTTP_404_NOT_FOUND)
        event.delete()
        return Response({"message": "Event Deleted"}, status.HTTP_200_OK)

