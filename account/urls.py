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
    path("student-info/<int:pk>/", UserAccountInfo.as_view()),
    path("student-count/", StudentCount.as_view()),
    path("current-student/<int:pk>/", CurrentLevelStudents.as_view()),
    path("all-lecturers/", ListLecturers.as_view()),
    path("user-social-links/", SocialLinkView.as_view()),
    path('update/', UpdateAccountView.as_view()),
]

