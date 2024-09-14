from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.template.loader import render_to_string

from .utils import *
from .models import *
from .serializers import *
from .permissions import (
    CreateAccountPerm
)

import os
from dotenv import load_dotenv

load_dotenv()

class DeleteUsers(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        users = Account.objects.all().delete()
        return Response({"message": "Deleted"}, status.HTTP_200_OK)

class CreateAccount(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        frontend_url = os.getenv("FRONTEND_BASE_URL")
        data = {}
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            user = serializer.save(is_admin_user=True)

            user.otp_token = generate_verification_token()
            user.save()

            context = {
                "name": user.first_name,
                "reset_link": f"{frontend_url}/account/{user.otp_token}/",
                "user_instance": "Admin",
                }
            
            template = render_to_string("account/account_confirmation.html", context)
            send_email(user.email, "ITDIMS: Admin Account Confirmation", template)
                
            data["message"] = "Account created successfully"
            data["user_info"] = AccountSerializer(user).data
            data["token"] = get_auth_token(user)
            return Response(data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        # return Response({"message": "Incomplete Fields."}, status.HTTP_400_BAD_REQUEST)


class CreateStudentAccount(APIView):

    def post(self, request):
        user = request.user
        frontend_url = os.getenv("FRONTEND_BASE_URL")
        data = {}
        if user.is_admin_or_lecturer():
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid(raise_exception=False):
                user = serializer.save()

                user.otp_token = generate_verification_token()
                user.save()

                context = {
                    "name": user.first_name,
                    "reset_link": f"{frontend_url}/account/{user.otp_token}/",
                    "user_instance": "Student",
                    }
                
                template = render_to_string("account/account_confirmation.html", context)
                send_email(user.email, "ITDIMS: Student Account Confirmation", template)
                    
                data["message"] = "Account created successfully"
                data["user_info"] = StudentSerializer(user).data
                return Response(data, status.HTTP_201_CREATED)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        return Response({"message": "You do not have the permission to create this user."}, status.HTTP_401_UNAUTHORIZED)
        # return Response({"message": "Incomplete Fields."}, status.HTTP_400_BAD_REQUEST)


class CreateLecturerAccount(APIView):

    def post(self, request):
        user = request.user
        frontend_url = os.getenv("FRONTEND_BASE_URL")
        data = {}
        if user.is_admin_or_lecturer():
            serializer = LecturerSerializer(data=request.data)
            if serializer.is_valid(raise_exception=False):
                user = serializer.save()

                user.otp_token = generate_verification_token()
                user.save()

                context = {
                    "name": user.first_name,
                    "reset_link": f"{frontend_url}/account/{user.otp_token}/",
                    "user_instance": "Lecturer",
                    }
                
                template = render_to_string("account/account_confirmation.html", context)
                send_email(user.email, "ITDIMS: Lecturer Account Confirmation", template)
                    
                data["message"] = "Account created successfully"
                data["user_info"] = LecturerSerializer(user).data
                return Response(data, status.HTTP_201_CREATED)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        return Response({"message": "You do not have the permission to create this user."}, status.HTTP_401_UNAUTHORIZED)
        # return Response({"message": "Incomplete Fields."}, status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = {}
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get("email", "")
            matric_number = serializer.validated_data.get("matric_number", "")
            password = serializer.validated_data.get("password")
            
            if email:
                try:
                    user = Account.objects.get(email=email)
                except Account.DoesNotExist:
                    return Response({"message": "User with this email doesn't exist."}, status=status.HTTP_400_BAD_REQUEST)

            elif matric_number:
                try:
                    student = Student.objects.get(matric_number=matric_number)
                    user = student.account
                except Student.DoesNotExist:
                    return Response({"message": "Student with this matric number doesn't exist."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"message": "Email or Matric Number required."}, status=status.HTTP_400_BAD_REQUEST)

            # if user.check_password(password):
            if user.password == password:
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
        send_email(email, "ITDIMS: Password Reset", template)
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

    def get(self, request):
        user = request.user
        if user.is_admin_user:
            serializer = AdminSerializer(user)
            return Response(serializer.data, status.HTTP_200_OK)
        
        try:
            lecturer = Lecturer.objects.get(user=user)
            serializer = LecturerSerializer(lecturer)
            return Response(serializer.data, status.HTTP_200_OK)
        except Lecturer.DoesNotExist:
            pass

        try:
            student = Student.objects.get(user=user)
            serializer = StudentSerializer(student)
            return Response(serializer.data, status.HTTP_200_OK)
        except Student.DoesNotExist:
            pass

        return Response({"message": "No Information on Account"}, status.HTTP_200_OK)
    
    def put(self, request):
        user = request.user
        if user.is_admin_user:
            serializer = AdminSerializer(user, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            lecturer = Lecturer.objects.get(user=user)
            serializer = LecturerSerializer(lecturer, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Lecturer.DoesNotExist:
            pass

        try:
            student = Student.objects.get(user=user)
            serializer = StudentSerializer(student, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            pass

        return Response({"message": "No Information on Account"}, status.HTTP_400_NOT_FOUND)


class UserAccountInfo(APIView):

    def get(self, request, pk):
        user = Account.objects.get(id=pk)
        try:
            student = Student.objects.get(user=user)
            serializer = StudentSerializer(student)
            return Response(serializer.data, status.HTTP_200_OK)
        except Student.DoesNotExist:
            pass

        try:
            lecturer = Lecturer.objects.get(user=user)
            serializer = LecturerSerializer(lecturer)
            return Response(serializer.data, status.HTTP_200_OK)
        except Lecturer.DoesNotExist:
            pass

        return Response({"message": "No User Found"}, status.HTTP_404_NOT_FOUND)
    
class StudentCount(APIView):

    def get(self, request):
        count = student_count()
        return Response(count, status.HTTP_200_OK)


class CurrentLevelStudents(APIView):

    def get(self, request, pk):
        students = Student.objects.filter(level_year=pk)
        if students:
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        return Response({"message": "No Students added yet."}, status.HTTP_200_OK)


class ListLecturers(APIView):

    def get(self, request):
        lecturers = Lecturer.objects.all()
        serializer = LecturerSerializer(lecturers, many=True)
        return Response(serializer.data, status.HTTP_200_OK)



class SocialLinkView(APIView):
    def get(self, request):
        user = request.user
        try:
            social_link = SocialLink.objects.filter(user=user)
            serializer = SocialLinkSerializer(social_link, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        except:
            return Response({"message": "No Social Link found."}, status.HTTP_200_OK)