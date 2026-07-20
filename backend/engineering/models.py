# backend/engineering/models.py

from django.db import models

from common.models import ActivatableModel, TimestampedModel
from rooms.models import Room
from staff.models import User


class EngineeringService(TimestampedModel, ActivatableModel):
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


class EngineeringRequest(TimestampedModel):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        ASSIGNED = "ASSIGNED", "Assigned"
        IN_PROGRESS = "IN_PROGRESS", "In Progress"
        COMPLETED = "COMPLETED", "Completed"
        CANCELLED = "CANCELLED", "Cancelled"

    room = models.ForeignKey(
        Room,
        on_delete=models.PROTECT,
        related_name="engineering_requests",
    )

    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="engineering_requests",
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )

    note = models.TextField(
        blank=True,
    )

    completed_at = models.DateTimeField(
        null=True,
        blank=True,
    )


class EngineeringRequestItem(models.Model):
    request = models.ForeignKey(
        EngineeringRequest,
        on_delete=models.CASCADE,
        related_name="items",
    )

    service = models.ForeignKey(
        EngineeringService,
        on_delete=models.PROTECT,
        related_name="request_items",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["request", "service"],
                name="unique_engineering_request_service",
            )
        ]
