# backend/rooms/serializers.py
from rest_framework import serializers

from rooms.models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            "id",
            "room_number",
            "floor",
            "room_type",
            "public_token",
            "is_active",
            "created_at",
            "updated_at",
        ]
