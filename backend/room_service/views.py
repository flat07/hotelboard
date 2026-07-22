# backend/room_service/views.py
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import (
    OrderingFilter,
    SearchFilter,
)
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .filters import RoomServiceOrderFilter
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


class RoomServiceOrderListApiView(ListAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = RoomServiceOrderSerializer

    queryset = RoomServiceOrder.objects.select_related(
        "room",
        "assigned_to",
    ).prefetch_related("items__menu_item")

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    ordering_fields = [
        "-created_at",
    ]

    ordering = [
        "-created_at",
    ]

    search_fields = [
        "room__room_number",
        "note",
        "assigned_to__username",
    ]

    filterset_class = RoomServiceOrderFilter


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
