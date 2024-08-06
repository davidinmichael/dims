from django.urls import path
from .views import *

urlpatterns = [
    path("", CourseListCreate.as_view()),
    path("<int:pk>/", CourseDetail.as_view()),
    path("course_count/", CourseCounts.as_view()),
    path("current_courses/", StudentCurrentSemesterCourses.as_view()),
    path("own_outstanding_courses/", UserOutstandingCourse.as_view()),
    path("add_outstanding_courses/", AddOutstandingCourse.as_view()),
    path("<str:level>/<str:semester>/", CoursesByLevelAndSemester.as_view()),
]