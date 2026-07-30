# tests/factories/rooms.py

import factory
from factory.django import DjangoModelFactory

from rooms.models import Room


class RoomFactory(DjangoModelFactory):
    class Meta:
        model = Room
        skip_postgeneration_save = True

    room_number = factory.Sequence(lambda n: f"{100 + n}")  # type: ignore
    floor = factory.LazyAttribute(  # type: ignore
        lambda obj: max(1, int(obj.room_number) // 100)
    )
    room_type = Room.RoomType.STANDARD
    is_active = True
