from rest_framework.views import APIView
from .serializer import NotificationSerializer
from .models import Notification
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.



class NotificationView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)