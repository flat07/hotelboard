from decimal import Decimal

import pytest
from rest_framework.test import APIClient

from room_service.models import MenuCategory, MenuItem, RoomServiceOrder
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


@pytest.fixture
def menu_items():
    category = MenuCategory.objects.create(name="Breakfast", display_order=1)
    omelette = MenuItem.objects.create(
        category=category,
        name="Omelette",
        price=Decimal("28.00"),
    )
    coffee = MenuItem.objects.create(
        category=category,
        name="Coffee",
        price=Decimal("12.00"),
    )
    return omelette, coffee


@pytest.mark.django_db
def test_guest_can_create_an_order_with_the_correct_total(
    api_client,
    room,
    menu_items,
):
    omelette, coffee = menu_items

    response = api_client.post(
        f"/api/v1/public/room-service/orders/{room.public_token}/",
        {
            "note": "Please bring extra ketchup.",
            "items": [
                {"menu_item": omelette.id, "quantity": 2},
                {"menu_item": coffee.id, "quantity": 1},
            ],
        },
        format="json",
    )

    assert response.status_code == 201
    assert response.data["status"] == RoomServiceOrder.Status.PENDING
    assert response.data["note"] == "Please bring extra ketchup."
    assert response.data["total_price"] == "68.00"

    order = RoomServiceOrder.objects.prefetch_related("items").get(
        pk=response.data["id"]
    )
    assert order.room == room
    assert order.total_price == Decimal("68.00")
    assert {
        (item.menu_item_id, item.quantity, item.price)
        for item in order.items.all()  # type: ignore
    } == {  # noqa: E501
        (omelette.id, 2, Decimal("28.00")),
        (coffee.id, 1, Decimal("12.00")),
    }


@pytest.mark.django_db
def test_guest_order_requires_at_least_one_item(api_client, room):
    response = api_client.post(
        f"/api/v1/public/room-service/orders/{room.public_token}/",
        {"items": []},
        format="json",
    )

    assert response.status_code == 400
    assert response.data == {"items": ["Order must contain at least one item."]}
    assert not RoomServiceOrder.objects.exists()


@pytest.mark.django_db
def test_guest_order_rejects_a_zero_quantity(api_client, room, menu_items):
    omelette, _ = menu_items

    response = api_client.post(
        f"/api/v1/public/room-service/orders/{room.public_token}/",
        {"items": [{"menu_item": omelette.id, "quantity": 0}]},
        format="json",
    )

    assert response.status_code == 400
    assert response.data == {
        "items": [{"quantity": ["Ensure this value is greater than or equal to 1."]}]
    }
    assert not RoomServiceOrder.objects.exists()
