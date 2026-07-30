import pytest
from rest_framework.test import APIClient

from hk.models import (
    HousekeepingRequest,
    HousekeepingRequestItem,
    HousekeepingService,
)
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
def housekeeping_services():
    return (
        HousekeepingService.objects.create(
            code="CLEAN_ROOM",
            name="Clean room",
        ),
        HousekeepingService.objects.create(
            code="EXTRA_TOWELS",
            name="Extra towels",
        ),
    )


@pytest.mark.django_db
def test_guest_can_create_a_housekeeping_request(
    api_client,
    room,
    housekeeping_services,
):
    clean_room, extra_towels = housekeeping_services

    response = api_client.post(
        f"/api/v1/public/housekeeping/requests/{room.public_token}/",
        {
            "note": "Please come after 2 PM.",
            "items": [
                {"service": clean_room.id},
                {"service": extra_towels.id},
            ],
        },
        format="json",
    )

    assert response.status_code == 201
    assert response.data["status"] == HousekeepingRequest.Status.PENDING
    assert response.data["note"] == "Please come after 2 PM."

    request = HousekeepingRequest.objects.get(pk=response.data["id"])
    assert request.room == room
    assert set(
        HousekeepingRequestItem.objects.filter(request=request).values_list(
            "service_id",
            flat=True,
        )
    ) == {clean_room.id, extra_towels.id}


@pytest.mark.django_db
def test_housekeeping_request_requires_at_least_one_service(api_client, room):
    response = api_client.post(
        f"/api/v1/public/housekeeping/requests/{room.public_token}/",
        {"items": []},
        format="json",
    )

    assert response.status_code == 400
    assert response.data == {"items": ["Please select at least one service."]}
    assert not HousekeepingRequest.objects.exists()
