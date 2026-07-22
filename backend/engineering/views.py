# backend/engineering/views.py
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .filters import EngineeringRequestFilter
from .models import (
    EngineeringRequest,
    EngineeringRequestItem,
    EngineeringService,
)
from .serializers import (
    EngineeringRequestItemSerializer,
    EngineeringRequestListSerializer,
    EngineeringRequestSerializer,
    EngineeringServiceSerializer,
)


class EngineeringRequestListAPIView(ListAPIView):
    permission_classes = [
        IsAuthenticated,
    ]

    serializer_class = EngineeringRequestListSerializer

    queryset = EngineeringRequest.objects.select_related(
        "room",
        "assigned_to",
    ).prefetch_related(
        "items__service",
    )

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_class = EngineeringRequestFilter

    search_fields = [
        "room__room_number",
        "note",
        "assigned_to__username",
    ]

    ordering_fields = [
        "created_at",
    ]

    ordering = [
        "-created_at",
    ]


class EngineeringServiceViewSet(viewsets.ModelViewSet):
    queryset = EngineeringService.objects.active()  # type: ignore
    serializer_class = EngineeringServiceSerializer


class EngineeringRequestViewSet(viewsets.ModelViewSet):
    queryset = EngineeringRequest.objects.select_related(
        "room",
        "assigned_to",
    ).prefetch_related(
        "items__service",
    )

    serializer_class = EngineeringRequestSerializer


class EngineeringRequestItemViewSet(viewsets.ModelViewSet):
    queryset = EngineeringRequestItem.objects.select_related(
        "request",
        "service",
    )

    serializer_class = EngineeringRequestItemSerializer
