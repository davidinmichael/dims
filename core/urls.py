from django.urls import path
from .views import NotificationView





urlpatterns = [
    path('user/notifications/', NotificationView.as_view(), name='notifications')
]