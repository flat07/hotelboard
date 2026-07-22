# backend/hk/serializers.py
from rest_framework import serializers

from hk.models import HousekeepingRequest


class HousekeepingRequestListSerializer(serializers.ModelSerializer):
    room_number = serializers.CharField(
        source="room.number",
        read_only=True,
    )

    assigned_to = serializers.CharField(
        source="assigned_to.username",
        read_only=True,
    )

    services = serializers.SerializerMethodField()

    class Meta:
        model = HousekeepingRequest

        fields = [
            "id",
            "room_number",
            "status",
            "assigned_to",
            "note",
            "services",
            "created_at",
        ]

    def get_services(self, obj):
        return [item.service.name for item in obj.items.all()]


class CreateHousekeepingRequestSerializer(
    serializers.Serializer,
):
    token = serializers.CharField(
        max_length=64,
    )

    services = serializers.ListField(
        child=serializers.CharField(),
        allow_empty=False,
    )

    note = serializers.CharField(
        required=False,
        allow_blank=True,
        default="",
    )
