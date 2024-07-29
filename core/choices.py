from django.db import models
from django.utils.translation import gettext_lazy as _


class Availability(models.TextChoices):
    AVAILABLE = "available", _("Available")
    UNAVAILABLE = "unavailable", _("Unavailable")


class StudentLevel(models.TextChoices):
    LEVEL_ONE = 1, _("Level One")
    LEVEL_TWO = 2, _("Level Two")
    LEVEL_THREE = 3, _("Level Three")
    LEVEL_FOUR = 4, _("Level Four")
    LEVEL_FIVE = 5, _("Level Five")



class SchoolSemester(models.TextChoices):
    FIRST_SEMESTER = "first_semester", _("First Semester")
    SECOND_SEMESTER = "second_semester", _("Second Semester")