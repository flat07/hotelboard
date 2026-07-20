# backend/hk/public/serializers.py
from rest_framework import serializers

from hk.models import HousekeepingRequest, HousekeepingService


class HousekeepingServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousekeepingService

        fields = [
            "id",
            "code",
            "name",
        ]


# [
#     {
#         "id": 1,
#         "code": "CLEAN_ROOM",
#         "name": "Clean Room"
#     },
#     {
#         "id": 2,
#         "code": "CHANGE_TOWELS",
#         "name": "Change Towels"
#     }
# ]


class CreateHousekeepingRequestItemSerializer(serializers.Serializer):
    service = serializers.IntegerField()


class CreateHousekeepingRequestSerializer(serializers.Serializer):
    note = serializers.CharField(
        required=False,
        allow_blank=True,
    )

    items = CreateHousekeepingRequestItemSerializer(
        many=True,
    )

    def validate_items(self, value):
        if not value:
            raise serializers.ValidationError("Please select at least one service.")

        return value


# {
#     "note": "Please come after 2 PM.",
#     "items": [
#         {
#             "service": 1
#         },
#         {
#             "service": 2
#         }
#     ]
# }


class HousekeepingRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousekeepingRequest

        fields = [
            "id",
            "status",
            "note",
            "created_at",
        ]


# {
#     "id": 15,
#     "status": "PENDING",
#     "note": "Please come after 2 PM.",
#     "created_at": "2026-07-18T11:15:00Z"
# }
