from django.db import models
from django.utils import timezone

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    venue_address = models.TextField()

    def __str__(self):
        return self.title
