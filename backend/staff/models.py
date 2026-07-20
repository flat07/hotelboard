# backend/staff/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        MANAGER = "MANAGER", "Manager"
        HOUSEKEEPING = "HOUSEKEEPING", "Housekeeping"
        ENGINEERING = "ENGINEERING", "Engineering"
        ROOM_SERVICE = "ROOM_SERVICE", "Room Service"

    role = models.CharField(
        max_length=30,
        choices=Role.choices,
        default=Role.HOUSEKEEPING,
    )

    def __str__(self):
        return self.get_full_name() or self.username
