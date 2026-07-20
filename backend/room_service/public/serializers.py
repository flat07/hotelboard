# backend/room_service/public/serializers.py
from rest_framework import serializers

from room_service.models import (
    MenuCategory,
    MenuItem,
    RoomServiceOrder,
)


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = [
            "id",
            "name",
            "description",
            "price",
        ]


class MenuCategorySerializer(serializers.ModelSerializer):
    items = MenuItemSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = MenuCategory
        fields = [
            "id",
            "name",
            "items",
        ]


# [
#     {
#         "id": 1,
#         "name": "Breakfast",
#         "items": [
#             {
#                 "id": 3,
#                 "name": "Omelette",
#                 "description": "",
#                 "price": "28.00"
#             }
#         ]
#     }
# ]


class CreateOrderItemSerializer(serializers.Serializer):
    menu_item = serializers.IntegerField()

    quantity = serializers.IntegerField(
        min_value=1,
        max_value=20,
    )


# {
#     "menu_item": 5,
#     "quantity": 2
# }


class CreateOrderSerializer(serializers.Serializer):
    note = serializers.CharField(
        required=False,
        allow_blank=True,
    )

    items = CreateOrderItemSerializer(
        many=True,
    )

    def validate_items(self, value):
        if not value:
            raise serializers.ValidationError("Order must contain at least one item.")

        return value


# {
#     "note": "Extra ketchup",
#     "items": [
#         {
#             "menu_item": 1,
#             "quantity": 2
#         },
#         {
#             "menu_item": 8,
#             "quantity": 1
#         }
#     ]
# }


class RoomServiceOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomServiceOrder

        fields = [
            "id",
            "status",
            "note",
            "total_price",
            "created_at",
        ]


# {
#     "id": 12,
#     "status": "PENDING",
#     "note": "Extra ketchup",
#     "total_price": "72.00",
#     "created_at": "2026-07-18T15:20:11Z"
# }
