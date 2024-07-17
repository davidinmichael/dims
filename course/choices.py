from django.db import models
from django.utils.translation import gettext_lazy as _

class Status(models.TextChoices):
    AVAILABLE = "available", _("Available")
    UNAVAILABLE = 'Unavailable', _('Unavailable')
    PENDING = 'Pending', _('Pending')
    COMPLETED = "completed", _("Completed")
