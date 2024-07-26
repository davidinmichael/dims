from django.urls import path
from .views import *


urlpatterns = [
    path("register/", CreateAccount.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
]
