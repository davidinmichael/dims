from django.urls import path
from .views import *


urlpatterns = [
    path("register/", CreateAccount.as_view()),
    path("login/", LoginView.as_view()),
    path("initiate-forgot-password/", InitiateForgotPassword.as_view()),
    path("set-new-password/", SetNewPassword.as_view()),
]
