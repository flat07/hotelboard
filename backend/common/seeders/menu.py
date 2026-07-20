# backend/common/seeders/menu.py

from decimal import Decimal

from room_service.models import MenuCategory, MenuItem


def seed_menu(command):
    categories = [
        {
            "name": "Breakfast",
            "display_order": 1,
            "items": [
                {
                    "name": "Continental Breakfast",
                    "description": "Croissant, butter, jam, juice, and coffee.",
                    "price": Decimal("45.00"),
                    "display_order": 1,
                },
                {
                    "name": "American Breakfast",
                    "description": "Eggs, beef bacon, hash browns, toast, and coffee.",
                    "price": Decimal("65.00"),
                    "display_order": 2,
                },
            ],
        },
        {
            "name": "Main Course",
            "display_order": 2,
            "items": [
                {
                    "name": "Grilled Chicken",
                    "description": "Served with mashed potatoes and vegetables.",
                    "price": Decimal("85.00"),
                    "display_order": 1,
                },
                {
                    "name": "Beef Burger",
                    "description": "Beef burger with fries.",
                    "price": Decimal("70.00"),
                    "display_order": 2,
                },
            ],
        },
        {
            "name": "Desserts",
            "display_order": 3,
            "items": [
                {
                    "name": "Chocolate Cake",
                    "description": "Rich chocolate cake.",
                    "price": Decimal("30.00"),
                    "display_order": 1,
                },
                {
                    "name": "Ice Cream",
                    "description": "Vanilla ice cream with chocolate sauce.",
                    "price": Decimal("25.00"),
                    "display_order": 2,
                },
            ],
        },
        {
            "name": "Beverages",
            "display_order": 4,
            "items": [
                {
                    "name": "Coffee",
                    "description": "Freshly brewed coffee.",
                    "price": Decimal("18.00"),
                    "display_order": 1,
                },
                {
                    "name": "Orange Juice",
                    "description": "Freshly squeezed orange juice.",
                    "price": Decimal("22.00"),
                    "display_order": 2,
                },
                {
                    "name": "Mineral Water",
                    "description": "500ml bottled water.",
                    "price": Decimal("10.00"),
                    "display_order": 3,
                },
            ],
        },
    ]

    for category_data in categories:
        category, _ = MenuCategory.objects.update_or_create(
            name=category_data["name"],
            defaults={
                "display_order": category_data["display_order"],
                "is_active": True,
            },
        )

        for item_data in category_data["items"]:
            MenuItem.objects.update_or_create(
                category=category,
                name=item_data["name"],
                defaults={
                    "description": item_data["description"],
                    "price": item_data["price"],
                    "is_available": True,
                    "display_order": item_data["display_order"],
                },
            )

    command.stdout.write(command.style.SUCCESS("✓ Menu seeded successfully."))
