from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.template.loader import render_to_string

from .utils import *
from .models import *
from .serializers import *


class CreateAccount(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = {}
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            user = serializer.save()
            
            # Handling nested SocialLinks
            social_links_data = request.data.get('social_links', [])
            for social_link_data in social_links_data:
                SocialLink.objects.create(user=user, **social_link_data)
                
            data["message"] = "Account created successfully"
            data["user_info"] = AccountSerializer(user).data
            data["token"] = get_auth_token(user)
            return Response(data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        # return Response({"message": "Incomplete Fields."}, status.HTTP_400_BAD_REQUEST)
        