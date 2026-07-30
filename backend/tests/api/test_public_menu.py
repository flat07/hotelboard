from decimal import Decimal

import pytest
from rest_framework.test import APIClient

from room_service.models import MenuCategory, MenuItem
from rooms.models import Room


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def room():
    return Room.objects.create(
        room_number="1205",
        floor=12,
        room_type=Room.RoomType.DELUXE,
    )


@pytest.mark.django_db
def test_guest_menu_returns_only_active_categories_in_display_order(api_client, room):
    later_category = MenuCategory.objects.create(name="Dinner", display_order=2)
    first_category = MenuCategory.objects.create(name="Breakfast", display_order=1)
    MenuCategory.objects.create(name="Archived", display_order=0, is_active=False)

    MenuItem.objects.create(
        category=later_category,
        name="Steak",
        price=Decimal("120.00"),
    )
    MenuItem.objects.create(
        category=first_category,
        name="Omelette",
        price=Decimal("28.00"),
    )

    response = api_client.get(f"/api/v1/public/room-service/menu/{room.public_token}/")

    assert response.status_code == 200
    assert [category["name"] for category in response.data] == ["Breakfast", "Dinner"]


@pytest.mark.django_db
def test_guest_menu_does_not_include_unavailable_items(api_client, room):
    category = MenuCategory.objects.create(name="Breakfast", display_order=1)
    available_item = MenuItem.objects.create(
        category=category,
        name="Omelette",
        price=Decimal("28.00"),
        is_available=True,
    )
    MenuItem.objects.create(
        category=category,
        name="Sold out coffee",
        price=Decimal("12.00"),
        is_available=False,
    )

    response = api_client.get(f"/api/v1/public/room-service/menu/{room.public_token}/")

    assert response.status_code == 200
    assert response.data[0]["items"] == [
        {
            "id": available_item.id,  # type: ignore
            "name": "Omelette",
            "description": "",
            "price": "28.00",
        }
    ]
