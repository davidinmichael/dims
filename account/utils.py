from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from .models import *
from .serializers import *

import random
import string


def generate_verification_token(*, length=4):
    return "".join(random.choices('123456789', k=length))


def get_auth_token(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


def send_email(user_email, subject, template):
    subject = subject
    from_email = settings.EMAIL_HOST_USER
    to_email = [user_email]

    email = EmailMultiAlternatives(
        subject = subject,
        body = "Email Content",
        from_email = from_email,
        to=to_email,
    )

    email.content_subtype = "html"
    email.attach_alternative(template, "text/html")

    try:
        email.send(fail_silently=False)
    except Exception as e:
        print("Email sending failed", {e})
        return "Couldn't connect, try again"
    return None


def student_count():
    level_1 = Student.objects.filter(level_year=1).count()
    level_2 = Student.objects.filter(level_year=2).count()
    level_3 = Student.objects.filter(level_year=3).count()
    level_4 = Student.objects.filter(level_year=4).count()
    level_5 = Student.objects.filter(level_year=5).count()

    data = {
        "level_1": level_1,
        "level_2": level_2,
        "level_3": level_3,
        "level_4": level_4,
        "level_5": level_5,
    }
    return data