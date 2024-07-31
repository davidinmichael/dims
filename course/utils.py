from .models import *
from .serializers import *


def total_and_semster_courses_count(user):
    data = {}
    total_courses = Courses.objects.filter(level__lte=user.level_year)
    total_courses_serializer = CourseSerializer(total_courses, many=True).data

    current_semester_courses = Courses.objects.filter(level=user.level_year, semester=user.current_semester)
    current_semester_courses_serializer = CourseSerializer(current_semester_courses, many=True).data

    outstanding_courses = OutstandingCourses.objects.get(user=user)
    outstanding_courses_serializer = OutstandingCourseSerializer(outstanding_courses).data

    data["total_course_count"] = total_courses.count()
    data["current_semester_course_count"] = current_semester_courses.count()
    data["outstanding_courses_count"] = outstanding_courses.count_courses()

    return data


def total_and_semster_courses(user):
    data = {}
    total_courses = Courses.objects.filter(level__lte=user.level_year)
    total_courses_serializer = CourseSerializer(total_courses, many=True).data

    current_semester_courses = Courses.objects.filter(level=user.level_year, semester=user.current_semester)
    current_semester_courses_serializer = CourseSerializer(current_semester_courses, many=True).data
 
    outstanding_courses = OutstandingCourses.objects.get(user=user)
    outstanding_courses_serializer = OutstandingCourseSerializer(outstanding_courses).data

    data["total_course_count"] = total_courses.count()
    data["current_semester_course_count"] = current_semester_courses.count()
    data["outstanding_courses_count"] = outstanding_courses.count_courses()

    data["total_courses"] = total_courses_serializer
    data["current_semester_courses"] = current_semester_courses_serializer
    data["outstanding_courses"] = outstanding_courses_serializer

    return data
    