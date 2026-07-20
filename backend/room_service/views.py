from rest_framework import viewsets

from .models import (
    MenuCategory,
    MenuItem,
    RoomServiceOrder,
    RoomServiceOrderItem,
)
from .serializers import (
    MenuCategorySerializer,
    MenuItemSerializer,
    RoomServiceOrderItemSerializer,
    RoomServiceOrderSerializer,
)


class MenuCategoryViewSet(viewsets.ModelViewSet):
    queryset = MenuCategory.objects.active()  # type: ignore

    serializer_class = MenuCategorySerializer


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.select_related(
        "category",
    )

    serializer_class = MenuItemSerializer


class RoomServiceOrderViewSet(viewsets.ModelViewSet):
    queryset = RoomServiceOrder.objects.select_related(
        "room",
        "assigned_to",
    ).prefetch_related(
        "items__menu_item",
    )

    serializer_class = RoomServiceOrderSerializer


class RoomServiceOrderItemViewSet(viewsets.ModelViewSet):
    queryset = RoomServiceOrderItem.objects.select_related(
        "order",
        "menu_item",
    )

    serializer_class = RoomServiceOrderItemSerializer
