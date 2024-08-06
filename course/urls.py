from django.urls import path
from .views import *

urlpatterns = [
    path("", CourseListCreate.as_view()),
    path("<int:pk>/", CourseDetail.as_view()),
    path("course_count/", CourseCounts.as_view()),
    path("own_courses/", UserOwnCourses.as_view()),
    path("own_outstanding_courses/", UserOutstandingCourse.as_view()),
    path("add_outstanding_courses/", AddOutstandingCourse.as_view()),
    path("courses/<str:level>/<str:semester>/", CoursesByLevelAndSemester.as_view()),
]