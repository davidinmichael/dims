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
                
            data["message"] = "Account created successfully"
            data["user_info"] = AccountSerializer(user).data
            data["token"] = get_auth_token(user)
            return Response(data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        # return Response({"message": "Incomplete Fields."}, status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = {}
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]

            try:
                user = Account.objects.get(email=email)
            except Account.DoesNotExist:
                return Response({"message": "User with this email doesn't exist."}, status.HTTP_400_BAD_REQUEST)
            
            if user.check_password(password):
                data["message"] = "Login successfully"
                data["user_info"] = AccountSerializer(user).data
                data["token"] = get_auth_token(user)
                return Response(data, status.HTTP_200_OK)
            return Response({"message": "Invalid Credentials"}, status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


