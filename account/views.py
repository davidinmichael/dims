from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.template.loader import render_to_string

from .utils import *
from .models import *
from .serializers import *

import os
from dotenv import load_dotenv

load_dotenv()


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



class InitiateForgotPassword(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        frontend_url = os.getenv("FRONTEND_BASE_URL")
        email = request.data.get("email")
        try:
            user = Account.objects.get(email=email)
        except Account.DoesNotExist:
            return Response({"message": "User with this email doesn't exist."}, status.HTTP_400_BAD_REQUEST)
        
        user.otp_token = generate_verification_token()
        user.save()

        context = {
            "name": user.first_name,
            "reset_link": f"{frontend_url}/account/{user.otp_token}/"
        }
        template = render_to_string("account/initiate_forgot_password.html", context)
        send_email(email, "DIMS: Password Reset", template)
        return Response({"message": "A link has been sent to your email."}, status.HTTP_200_OK)
            

class SetNewPassword(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SetNewPasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data
            try:
                user = Account.objects.get(otp_token=data["otp_token"])
            except Account.DoesNotExist:
                return Response({"message": "Invalid or Expired Link"}, status.HTTP_400_BAD_REQUEST)
            
            user.set_password(data["password"])
            user.save()
            return Response({"message": "Password Updated Successfully"}, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.is_admin_user:
            serializer = AdminSerializer(user)
        elif user.is_lecturer:
            serializer = LecturerSerializer(user)
        elif user.is_student:
            serializer = StudentSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)