import pytest
from rest_framework.test import APIClient

from engineering.models import (
    EngineeringRequest,
    EngineeringRequestItem,
    EngineeringService,
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
def engineering_services():
    return (
        EngineeringService.objects.create(
            code="AIR_CONDITIONING",
            name="Air conditioning",
        ),
        EngineeringService.objects.create(
            code="PLUMBING",
            name="Plumbing",
        ),
    )


@pytest.mark.django_db
def test_guest_can_create_an_engineering_request(
    api_client,
    room,
    engineering_services,
):
    air_conditioning, plumbing = engineering_services

    response = api_client.post(
        f"/api/v1/public/engineering/requests/{room.public_token}/",
        {
            "note": "The air conditioner is leaking.",
            "items": [
                {"service": air_conditioning.id},
                {"service": plumbing.id},
            ],
        },
        format="json",
    )

    assert response.status_code == 201
    assert response.data["status"] == EngineeringRequest.Status.PENDING
    assert response.data["note"] == "The air conditioner is leaking."

    request = EngineeringRequest.objects.get(pk=response.data["id"])
    assert request.room == room
    assert set(
        EngineeringRequestItem.objects.filter(request=request).values_list(
            "service_id",
            flat=True,
        )
    ) == {air_conditioning.id, plumbing.id}


@pytest.mark.django_db
def test_engineering_request_requires_at_least_one_service(api_client, room):
    response = api_client.post(
        f"/api/v1/public/engineering/requests/{room.public_token}/",
        {"items": []},
        format="json",
    )

    assert response.status_code == 400
    assert response.data == {"items": ["Please select at least one service."]}
    assert not EngineeringRequest.objects.exists()
