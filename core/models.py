from django.db import models
from account.models import Account
# Create your models here.


class Notification(models.Model):
    message = models.CharField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.first_name} {self.user.last_name}: {self.message}"