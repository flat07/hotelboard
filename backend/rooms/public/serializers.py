# backend/rooms/public/serializers.py
from rest_framework import serializers

from rooms.models import Room
from rooms.public.exceptions import (
    RoomNotFoundError,
)
from rooms.public.services import (
    get_room_by_token,
)


class RoomLookupSerializer(serializers.Serializer):
    token = serializers.CharField(
        max_length=64,
    )

    def validate_token(self, value):
        try:
            room = get_room_by_token(value)
        except RoomNotFoundError as err:
            raise serializers.ValidationError("Invalid room token.") from err

        self.context["room"] = room

        return value


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            "room_number",
            "room_type",
        ]
