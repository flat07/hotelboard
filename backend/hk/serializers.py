# backend/hk/serializers.py
from rest_framework import serializers


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
