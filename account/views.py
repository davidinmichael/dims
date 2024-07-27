from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail

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
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            # Assuming get_auth_token is a utility function to get JWT token
            token = get_auth_token(user)
            data = {
                "token": token,
                "user_info": AccountSerializer(user).data
            }
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
     
     
class ForgotPasswordView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        matric_number = request.data.get('matric_number')
        email = request.data.get('email')
        if not matric_number or not email:
            return Response({"error": "Matric number and email are required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = Account.objects.get(matric_number=matric_number, email=email)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            # Assume `password_reset_email.html` is your email template
            context = {
                'user': user,
                'uid': uid,
                'token': token
            }
            subject = 'Password Reset Requested'
            message = render_to_string('password_reset_email.html', context)
            send_mail(subject, message, 'from@example.com', [user.email], fail_silently=False)
            return Response({"message": "Password reset email sent"}, status=status.HTTP_200_OK)
        except Account.DoesNotExist:
            return Response({"error": "User with this matric number and email does not exist"}, status=status.HTTP_400_BAD_REQUEST)