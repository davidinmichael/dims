from django.db import models
from account.models import Account
# Create your models here.


class Notification(models.Model):
    user = models.ForeignKey(Account, related_name="lecturer_courses", on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField
    created_at = models.DateTimeField(auto_now=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.first_name} {self.user.last_name}: {self.message}"