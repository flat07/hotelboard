import pytest

from rooms.models import Room
from rooms.public.exceptions import RoomNotFoundError
from rooms.public.services import get_room_by_token

pytestmark = pytest.mark.django_db


class TestGetRoomByToken:
    def test_returns_active_room(self):
        room = Room.objects.create(
            room_number="1205",
            floor=12,
            room_type=Room.RoomType.DELUXE,
            is_active=True,
        )

        result = get_room_by_token(room.public_token)

        assert result == room

    def test_raises_error_when_room_does_not_exist(self):
        with pytest.raises(RoomNotFoundError, match="Invalid room token."):
            get_room_by_token("invalid-token")

    def test_raises_error_when_room_is_inactive(self):
        room = Room.objects.create(
            room_number="1206",
            floor=12,
            room_type=Room.RoomType.STANDARD,
            is_active=False,
        )

        with pytest.raises(RoomNotFoundError, match="Invalid room token."):
            get_room_by_token(room.public_token)
