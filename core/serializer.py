from rest_framework import serializers
from .models import Notification, IsReadNotification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"


class IsReadNotificationSerializer(serializers.ModelSerializer):
    notification = NotificationSerializer(required=True)
    class Meta:
        model = IsReadNotification
        fields = ["id", "notification", "read_at"]