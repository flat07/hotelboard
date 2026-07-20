from rest_framework import serializers

from .models import (
    EngineeringRequest,
    EngineeringRequestItem,
    EngineeringService,
)


class EngineeringServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineeringService
        fields = "__all__"


class EngineeringRequestItemSerializer(serializers.ModelSerializer):
    service_name = serializers.CharField(
        source="service.name",
        read_only=True,
    )

    class Meta:
        model = EngineeringRequestItem
        fields = [
            "id",
            "service",
            "service_name",
        ]


class EngineeringRequestSerializer(serializers.ModelSerializer):
    room_number = serializers.CharField(
        source="room.room_number",
        read_only=True,
    )

    assigned_to_name = serializers.CharField(
        source="assigned_to.get_full_name",
        read_only=True,
    )

    items = EngineeringRequestItemSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = EngineeringRequest
        fields = [
            "id",
            "room",
            "room_number",
            "assigned_to",
            "assigned_to_name",
            "status",
            "note",
            "completed_at",
            "created_at",
            "updated_at",
            "items",
        ]
