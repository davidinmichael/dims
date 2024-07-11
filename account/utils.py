from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.conf import settings


def get_auth_token(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }