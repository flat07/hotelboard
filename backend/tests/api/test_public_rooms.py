import pytest
from rest_framework.test import APIClient

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
def test_guest_can_look_up_an_active_room_with_its_public_token(api_client, room):
    response = api_client.get(f"/api/v1/public/rooms/guest/{room.public_token}/")

    assert response.status_code == 200
    assert response.data == {
        "room_number": "1205",
        "room_type": Room.RoomType.DELUXE,
    }
    assert "public_token" not in response.data


@pytest.mark.django_db
def test_guest_room_lookup_rejects_an_invalid_token(api_client):
    response = api_client.get("/api/v1/public/rooms/guest/not-a-valid-token/")

    assert response.status_code == 400
    assert response.data == {"token": ["Invalid room token."]}


@pytest.mark.django_db
def test_guest_room_lookup_rejects_an_inactive_room_token(api_client, room):
    room.is_active = False
    room.save(update_fields=["is_active"])

    response = api_client.get(f"/api/v1/public/rooms/guest/{room.public_token}/")

    assert response.status_code == 400
    assert response.data == {"token": ["Invalid room token."]}
