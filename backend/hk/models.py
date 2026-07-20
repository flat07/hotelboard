# backend/hk/models.py
from django.db import models

from common.models import ActivatableModel, TimestampedModel
from rooms.models import Room
from staff.models import User


class HousekeepingRequest(TimestampedModel):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        ASSIGNED = "ASSIGNED", "Assigned"
        COMPLETED = "COMPLETED", "Completed"

    room = models.ForeignKey(
        Room,
        on_delete=models.PROTECT,
        related_name="housekeeping_requests",
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="housekeeping_requests",
    )
    note = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Room {self.room}"


class HousekeepingService(TimestampedModel, ActivatableModel):
    code = models.CharField(
        max_length=50,
        unique=True,
    )

    name = models.CharField(
        max_length=100,
    )

    display_order = models.PositiveSmallIntegerField(
        default=1,
    )

    class Meta:
        ordering = [
            "display_order",
            "name",
        ]

    def __str__(self):
        return self.name


class HousekeepingRequestItem(models.Model):
    request = models.ForeignKey(
        HousekeepingRequest,
        on_delete=models.CASCADE,
        related_name="items",
    )

    service = models.ForeignKey(
        HousekeepingService,
        on_delete=models.PROTECT,
        related_name="request_items",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "request",
                    "service",
                ],
                name="unique_request_service",
            )
        ]

    def __str__(self):
        return str(self.request)
