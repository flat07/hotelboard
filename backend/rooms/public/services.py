# backend/rooms/public/services.py
from django.core.exceptions import ObjectDoesNotExist

from rooms.models import Room
from rooms.public.exceptions import RoomNotFoundError


def get_room_by_token(token: str) -> Room:
    """
    Return an active room using its public QR token.
    """

    try:
        return Room.objects.active().by_token(token)  # type: ignore

    except ObjectDoesNotExist as err:
        raise RoomNotFoundError("Invalid room token.") from err
