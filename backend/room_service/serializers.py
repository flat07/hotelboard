from rest_framework import serializers

from .models import (
    MenuCategory,
    MenuItem,
    RoomServiceOrder,
    RoomServiceOrderItem,
)


class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = "__all__"


class MenuItemSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source="category.name",
        read_only=True,
    )

    class Meta:
        model = MenuItem
        fields = [
            "id",
            "category",
            "category_name",
            "name",
            "description",
            "price",
            "is_available",
            "display_order",
        ]


class RoomServiceOrderItemSerializer(serializers.ModelSerializer):
    menu_item_name = serializers.CharField(
        source="menu_item.name",
        read_only=True,
    )

    class Meta:
        model = RoomServiceOrderItem
        fields = [
            "id",
            "menu_item",
            "menu_item_name",
            "quantity",
            "price",
        ]


class RoomServiceOrderSerializer(serializers.ModelSerializer):
    room_number = serializers.CharField(
        source="room.room_number",
        read_only=True,
    )

    assigned_to_name = serializers.CharField(
        source="assigned_to.get_full_name",
        read_only=True,
    )

    items = RoomServiceOrderItemSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = RoomServiceOrder
        fields = [
            "id",
            "room",
            "room_number",
            "assigned_to",
            "assigned_to_name",
            "status",
            "note",
            "total_price",
            "created_at",
            "updated_at",
            "items",
        ]
