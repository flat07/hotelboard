# backend/room_service/models.py

from decimal import Decimal

from django.db import models

from common.models import ActivatableModel, TimestampedModel
from rooms.models import Room
from staff.models import User


class MenuCategory(ActivatableModel):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    display_order = models.PositiveSmallIntegerField(
        default=1,
    )


class MenuItem(models.Model):
    category = models.ForeignKey(
        MenuCategory,
        on_delete=models.PROTECT,
        related_name="items",
    )

    name = models.CharField(
        max_length=100,
    )

    description = models.TextField(
        blank=True,
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )

    is_available = models.BooleanField(
        default=True,
    )

    display_order = models.PositiveSmallIntegerField(
        default=1,
    )


class RoomServiceOrder(TimestampedModel):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        PREPARING = "PREPARING", "Preparing"
        READY = "READY", "Ready"
        DELIVERED = "DELIVERED", "Delivered"
        CANCELLED = "CANCELLED", "Cancelled"

    room = models.ForeignKey(
        Room,
        on_delete=models.PROTECT,
        related_name="room_service_orders",
    )

    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="room_service_orders",
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )

    note = models.TextField(
        blank=True,
    )

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal("0.00"),
    )


class RoomServiceOrderItem(models.Model):
    order = models.ForeignKey(
        RoomServiceOrder,
        on_delete=models.CASCADE,
        related_name="items",
    )

    menu_item = models.ForeignKey(
        MenuItem,
        on_delete=models.PROTECT,
        related_name="order_items",
    )

    quantity = models.PositiveSmallIntegerField(
        default=1,
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )
