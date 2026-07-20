from rest_framework import viewsets

from .models import (
    EngineeringRequest,
    EngineeringRequestItem,
    EngineeringService,
)
from .serializers import (
    EngineeringRequestItemSerializer,
    EngineeringRequestSerializer,
    EngineeringServiceSerializer,
)


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
