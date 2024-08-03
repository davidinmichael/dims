from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Account
from course.models import OutstandingCourses


@receiver(post_save, sender=Account)
def create_outstanding_course(sender, instance, created, **kwargs):
    if created:
        instance.profile_url = f"account/me/{instance.id}"
        instance.save()
        OutstandingCourses.objects.create(user=instance)
