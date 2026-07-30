# backend/room_service/public/services.py
from decimal import Decimal

from django.db import transaction
from django.db.models import Prefetch

from room_service.models import (
    MenuCategory,
    MenuItem,
    RoomServiceOrder,
    RoomServiceOrderItem,
)
from rooms.models import Room


def get_menu_categories():
    return (
        MenuCategory.objects.filter(
            is_active=True,
        )
        .prefetch_related(
            Prefetch(
                "items",
                queryset=MenuItem.objects.filter(
                    is_available=True,
                ).order_by(
                    "display_order",
                    "name",
                ),
            ),
        )
        .order_by(
            "display_order",
        )
    )


@transaction.atomic
def create_room_service_order(
    *,
    room: Room,
    validated_data: dict,
) -> RoomServiceOrder:
    items_data = validated_data.pop("items")

    order = RoomServiceOrder.objects.create(
        room=room,
        note=validated_data.get("note", ""),
    )

    total = Decimal("0.00")

    for item_data in items_data:
        menu_item = MenuItem.objects.get(
            pk=item_data["menu_item"],
            is_available=True,
        )

        quantity = item_data["quantity"]

        RoomServiceOrderItem.objects.create(
            order=order,
            menu_item=menu_item,
            quantity=quantity,
            price=menu_item.price,
        )

        total += menu_item.price * quantity

    order.total_price = total
    order.save(
        update_fields=[
            "total_price",
        ]
    )

    return order
