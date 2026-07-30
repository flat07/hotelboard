# backend/tests/api/test_staff_rooms.py
import pytest
from rest_framework import status
from rest_framework.test import APIClient

from rooms.models import Room
from tests.factories.rooms import RoomFactory
from tests.factories.staff import StaffFactory

pytestmark = pytest.mark.django_db


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def staff():
    return StaffFactory()


@pytest.fixture
def auth_client(client, staff):
    response = client.post(
        "/api/v1/staff/auth/login/",
        {
            "username": staff.username,
            "password": "password123",
        },
        format="json",
    )

    assert response.status_code == 200

    access = response.data["access"]

    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")

    return client


class TestRoomList:
    endpoint = "/api/v1/staff/rooms/rooms/"

    def test_returns_room_list(self, auth_client):
        RoomFactory.create_batch(3)

        response = auth_client.get(self.endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 3


class TestRoomRetrieve:
    endpoint = "/api/v1/staff/rooms/rooms/"

    def test_returns_room(self, auth_client):
        room = RoomFactory()

        response = auth_client.get(f"{self.endpoint}{room.id}/")

        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == room.id
        assert response.data["room_number"] == room.room_number


class TestRoomCreate:
    endpoint = "/api/v1/staff/rooms/rooms/"

    def test_creates_room(self, auth_client):
        payload = {
            "room_number": "1205",
            "floor": 12,
            "room_type": Room.RoomType.DELUXE,
            "is_active": True,
        }

        response = auth_client.post(
            self.endpoint,
            payload,
            format="json",
        )

        assert response.status_code == status.HTTP_201_CREATED

        room = Room.objects.get(room_number="1205")

        assert room.floor == 12
        assert room.room_type == Room.RoomType.DELUXE
        assert room.is_active is True
        assert room.public_token


class TestRoomCreateValidation:
    endpoint = "/api/v1/staff/rooms/rooms/"

    def test_rejects_duplicate_room_number(self, auth_client):
        RoomFactory(room_number="1205")

        payload = {
            "room_number": "1205",
            "floor": 12,
            "room_type": Room.RoomType.DELUXE,
            "is_active": True,
        }

        response = auth_client.post(
            self.endpoint,
            payload,
            format="json",
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "room_number" in response.data


class TestRoomUpdate:
    endpoint = "/api/v1/staff/rooms/rooms/"

    def test_updates_room(self, auth_client):
        room = RoomFactory()

        payload = {
            "floor": 15,
        }

        response = auth_client.patch(
            f"{self.endpoint}{room.id}/",
            payload,
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK

        room.refresh_from_db()

        assert room.floor == 15


class TestRoomDelete:
    endpoint = "/api/v1/staff/rooms/rooms/"

    def test_deletes_room(self, auth_client):
        room = RoomFactory()

        response = auth_client.delete(f"{self.endpoint}{room.id}/")

        assert response.status_code == status.HTTP_204_NO_CONTENT

        assert not Room.objects.filter(id=room.id).exists()


class TestRoomNotFound:
    endpoint = "/api/v1/staff/rooms/rooms/"

    def test_returns_404(self, auth_client):
        response = auth_client.get(f"{self.endpoint}9999/")

        assert response.status_code == status.HTTP_404_NOT_FOUND
