from django.urls import path
from .views import CourseListCreate, CourseDetail

urlpatterns = [
    path('', CourseListCreate.as_view(), name='course-list'),
    path('<int:pk>/', CourseDetail.as_view(), name='course-detail'),
]