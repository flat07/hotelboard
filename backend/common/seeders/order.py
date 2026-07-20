# backend/common/seeders/order.py

from decimal import Decimal

from room_service.models import (
    MenuItem,
    RoomServiceOrder,
    RoomServiceOrderItem,
)
from rooms.models import Room
from staff.models import User


def seed_order(command):
    room101 = Room.objects.get(room_number="101")
    room102 = Room.objects.get(room_number="102")
    room201 = Room.objects.get(room_number="201")

    room_service_staff = User.objects.get(
        username="roomservice",
    )

    orders = [
        {
            "room": room101,
            "assigned_to": room_service_staff,
            "status": RoomServiceOrder.Status.PREPARING,
            "note": "Please bring extra ketchup.",
            "items": [
                ("Beef Burger", 2),
                ("Coffee", 2),
            ],
        },
        {
            "room": room102,
            "assigned_to": room_service_staff,
            "status": RoomServiceOrder.Status.DELIVERED,
            "note": "",
            "items": [
                ("American Breakfast", 1),
                ("Orange Juice", 1),
            ],
        },
        {
            "room": room201,
            "assigned_to": None,
            "status": RoomServiceOrder.Status.PENDING,
            "note": "No onions please.",
            "items": [
                ("Grilled Chicken", 1),
                ("Mineral Water", 2),
                ("Chocolate Cake", 1),
            ],
        },
    ]

    for order_data in orders:
        order = RoomServiceOrder.objects.create(
            room=order_data["room"],
            assigned_to=order_data["assigned_to"],
            status=order_data["status"],
            note=order_data["note"],
        )

        total = Decimal("0.00")

        for item_name, quantity in order_data["items"]:
            menu_item = MenuItem.objects.get(
                name=item_name,
            )

            RoomServiceOrderItem.objects.create(
                order=order,
                menu_item=menu_item,
                quantity=quantity,
                price=menu_item.price,
            )

            total += menu_item.price * quantity

        order.total_price = total
        order.save(update_fields=["total_price"])

    command.stdout.write(
        command.style.SUCCESS("✓ Room service orders seeded successfully.")
    )
