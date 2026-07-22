from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import (
    OrderingFilter,
    SearchFilter,
)
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from hk.models import HousekeepingRequest

from .filters import HousekeepingRequestFilter
from .serializers import (
    CreateHousekeepingRequestSerializer,
    HousekeepingRequestListSerializer,
)
from .services import (
    create_housekeeping_request,
)


class HousekeepingRequestListAPIView(
    ListAPIView,
):
    permission_classes = [
        IsAuthenticated,
    ]

    serializer_class = HousekeepingRequestListSerializer

    queryset = HousekeepingRequest.objects.select_related(
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
    ordering_fields = [
        "created_at",
    ]

    ordering = [
        "-created_at",
    ]

    search_fields = [
        "room__room_number",
        "note",
        "assigned_to__username",
    ]

    filterset_class = HousekeepingRequestFilter


class CreateHousekeepingRequestAPIView(APIView):
    def post(
        self,
        request,
    ):
        serializer = CreateHousekeepingRequestSerializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        housekeeping_request = create_housekeeping_request(
            **serializer.validated_data  # type: ignore
        )

        return Response(
            {
                "id": housekeeping_request.id,
                "message": "Request created.",
            },
            status=status.HTTP_201_CREATED,
        )
