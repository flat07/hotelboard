# backend/engineering/public/serializers.py

from rest_framework import serializers

from engineering.models import (
    EngineeringRequest,
    EngineeringService,
)


class EngineeringServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineeringService
        fields = [
            "id",
            "code",
            "name",
        ]


class CreateEngineeringRequestItemSerializer(serializers.Serializer):
    service = serializers.IntegerField()


class CreateEngineeringRequestSerializer(serializers.Serializer):
    note = serializers.CharField(
        required=False,
        allow_blank=True,
    )

    items = CreateEngineeringRequestItemSerializer(
        many=True,
    )

    def validate_items(self, value):
        if not value:
            raise serializers.ValidationError("Please select at least one service.")

        return value


class EngineeringRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineeringRequest
        fields = [
            "id",
            "status",
            "note",
            "created_at",
            "completed_at",
        ]


class EngineeringRequestItemSerializer(serializers.Serializer):
    name = serializers.CharField()


class EngineeringRequestDetailsSerializer(serializers.ModelSerializer):
    items = EngineeringRequestItemSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = EngineeringRequest
        fields = [
            "id",
            "status",
            "note",
            "created_at",
            "completed_at",
            "items",
        ]
