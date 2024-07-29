from django.db import models
from django.utils.translation import gettext_lazy as _

class Gender(models.TextChoices):
    FEMALE = "female", _("Female")
    MALE = "male", _("Male")
    OTHER = "other", _("Other")

class Availability(models.TextChoices):
    AVAILABLE = "available", _("Available")
    UNAVAILABLE = "unavailable", _("Unavailable")


class Qualification(models.TextChoices):
    SSCE = "ssce", _("SSCE")
    UNDERGRADUATE = "undergraduate", _("Undergraduate")
    OND = "ond", _("OND")
    HND = "hnd", _("HND")
    BACHELORS = "bachelors", _("Bachelors")
    MASTERS = "masters", _("Masters")
    PHD = "phd", _("PhD")
    OTHER = "other", _("Other")