from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework  import status

from .serializers import *
from .models import *


class ResourceView(APIView):

    def post(self, request):
        user = request.user
        serializer = ResourceSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            if user.is_admin_or_lecturer():
                resource = serializer.save(added_by=request.user)
                resource_serializer = ResourceSerializer(resource)
                return Response(resource_serializer.data, status.HTTP_201_CREATED)
            return Response({"message": "You do not have permissions to add a Resource."}, status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

