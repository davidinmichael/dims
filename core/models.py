from django.db import models
from account.models import Account


class Notification(models.Model):
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message


class IsReadNotification(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE, null=True, blank=True)
    read_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} | {self.notification.message}"