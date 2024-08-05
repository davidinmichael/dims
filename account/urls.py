from django.urls import path
from .views import *


urlpatterns = [
    path("delete/", DeleteUsers.as_view()),
    path("register/", CreateAccount.as_view()),
    path("register-student/", CreateStudentAccount.as_view()),
    path("register-lecturer/", CreateLecturerAccount.as_view()),
    path("login/", LoginView.as_view()),
    path("initiate-forgot-password/", InitiateForgotPassword.as_view()),
    path("set-new-password/", SetNewPassword.as_view()),
    path("profile/", ProfileView.as_view()),
]
