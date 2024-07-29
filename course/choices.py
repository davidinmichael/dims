from django.db import models
from django.utils.translation import gettext_lazy as _


class StudentLevel(models.TextChoices):
    LEVEL_ONE = "level_one", _("Level One")
    LEVEL_TWO = "level_two", _("Level Two")
    LEVEL_THREE = "level_three", _("Level Three")
    LEVEL_FOUR = "level_four", _("Level Four")
    LEVEL_FIVE = "level_five", _("Level Five")
