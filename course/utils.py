from .models import *
from .serializers import *


def total_and_semester_courses_count(user):
    data = {}
    total_courses = Courses.objects.filter(level__lte=user.level_year)
    current_semester_courses = Courses.objects.filter(level=user.level_year, semester=user.current_semester)
    
    try:
        outstanding_courses = OutstandingCourses.objects.get(user=user)
        outstanding_courses_count = outstanding_courses.count_courses()
    except OutstandingCourses.DoesNotExist:
        outstanding_courses_count = 0

    data["total_course_count"] = total_courses.count()
    data["current_semester_course_count"] = current_semester_courses.count()
    data["outstanding_courses_count"] = outstanding_courses_count

    return data



def total_and_semester_courses(user):
    data = {}
    total_courses = Courses.objects.filter(level__lte=user.level_year)
    total_courses_serializer = CourseSerializer(total_courses, many=True).data

    current_semester_courses = Courses.objects.filter(level=user.level_year, semester=user.current_semester)
    current_semester_courses_serializer = CourseSerializer(current_semester_courses, many=True).data
    
    try:
        outstanding_courses = OutstandingCourses.objects.get(user=user)
        outstanding_courses_serializer = OutstandingCourseSerializer(outstanding_courses).data
        data["outstanding_courses_count"] = outstanding_courses.courses.count()
    except OutstandingCourses.DoesNotExist:
        outstanding_courses_serializer = "No Outstanding Courses"
        data["outstanding_courses_count"] = 0

    data["total_course_count"] = total_courses.count()
    data["current_semester_course_count"] = current_semester_courses.count()
    data["total_courses"] = total_courses_serializer
    data["current_semester_courses"] = current_semester_courses_serializer
    data["outstanding_courses"] = outstanding_courses_serializer

    return data

    