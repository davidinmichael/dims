from django.db import models
from django.utils.translation import gettext_lazy as _

class Status(models.TextChoices):
    AVAILABLE = "available", _("Available")
    ACTIVE = "active", _("Active")