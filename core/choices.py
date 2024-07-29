from django.db import models
from django.utils.translation import gettext_lazy as _


class Availability(models.TextChoices):
    AVAILABLE = "available", _("Available")
    UNAVAILABLE = "unavailable", _("Unavailable")