from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.conf import settings


def get_auth_token(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


def send_email(user_email, template, subject):
    subject = subject
    from_email = settings.EMAIL_HOST_USER
    to_email = [user_email]

    email = EmailMultiAlternatives(
        subject = subject,
        body = "This is the body of the email",
        from_email = from_email,
        to=to_email,
    )

    email.content_subtype = "text/html"
    email.attach_alternative(template, "text/html")

    try:
        email.send(fail_silently=False)
    except Exception as e:
        print("Email sending failed", {e})
        return "Couldn't connect, try again"
    return None