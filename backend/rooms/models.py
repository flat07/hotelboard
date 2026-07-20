# backend/rooms/models.py
import secrets

from django.db import models

from common.models import TimestampedModel


class RoomQuerySet(models.QuerySet):
    def active(self):
        return self.filter(
            is_active=True,
        )

    def by_token(self, token):
        return self.get(
            public_token=token,
        )


class RoomManager(
    models.Manager.from_queryset(
        RoomQuerySet,
    )
):
    pass


def generate_public_token():
    return secrets.token_urlsafe(32)


class Room(TimestampedModel):
    class RoomType(models.TextChoices):
        STANDARD = (
            "STANDARD",
            "Standard",
        )

        DELUXE = (
            "DELUXE",
            "Deluxe",
        )

        SUITE = (
            "SUITE",
            "Suite",
        )

    room_number = models.CharField(
        max_length=10,
        unique=True,
    )

    floor = models.PositiveSmallIntegerField()

    room_type = models.CharField(
        max_length=20,
        choices=RoomType.choices,
    )
    public_token = models.CharField(
        max_length=64,
        unique=True,
        default=generate_public_token,
        editable=False,
    )

    is_active = models.BooleanField(
        default=True,
    )
    objects = RoomManager()

    class Meta:
        ordering = ["room_number"]

        indexes = [
            models.Index(
                fields=["public_token"],
            ),
        ]

    def __str__(self):
        return self.room_number
