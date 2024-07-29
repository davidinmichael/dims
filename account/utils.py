from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from course.models import Courses

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


def student_courses(student):
    current_level = int(student.level_year)
    total_courses = Courses.objects.filter(level__lte=current_level)
    current_semester = student.current_semester
    current_semester_courses = total_courses.filter(semester=current_semester)
    
    completed_courses = student.completed_courses.all()
    outstanding_courses = total_courses.exclude(id__in=completed_courses.values_list('id', flat=True))

    response = {
        "current_level": current_level,
        "current_semester": current_semester,
        "total_courses": {
            "count": total_courses.count(),
            "courses": list(total_courses.values('course_title', 'course_code', 'lecture_date', 'lecture_time'))
        },
        "current_semester_courses": {
            "count": current_semester_courses.count(),
            "courses": list(current_semester_courses.values('course_title', 'course_code', 'lecture_date', 'lecture_time'))
        },
        "outstanding_courses": {
            "count": outstanding_courses.count(),
            "courses": list(outstanding_courses.values('course_title', 'course_code', 'lecture_date', 'lecture_time'))
        }
    }

    return response