from functools import partial
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .serializers import *
from .models import Event

class EventListCreatedView(APIView):

    def get(self, request):
        events = Event.objects.all()
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
            
        
    

# class EventUpdateView(LoginRequiredMixin, APIView):
#     """
#     API view to update an existing event (requires login).
#     """
#     permission_classes = [IsAuthenticated, IsCustomAdminUser]

#     def put(self, request, pk):
#         event = get_object_or_404(Event, pk=pk, user=request.user)
#         data = json.loads(request.body)
#         serializer = EventSerializer(event, data=data, partial=True)
#         if serializer.is_valid():
#             event = serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)


# class EventDeleteView(LoginRequiredMixin, APIView):
#     """
#     API view to delete an existing event (requires login).
#     """
#     permission_classes = [IsAuthenticated, IsCustomAdminUser]

#     def delete(self, request, pk):
#         event = get_object_or_404(Event, pk=pk, user=request.user)
#         event.delete()
#         return JsonResponse({'message': 'Event deleted successfully'})
