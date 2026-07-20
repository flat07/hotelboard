# backend/hk/public/views.py
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from rooms.public.serializers import RoomLookupSerializer

from .serializers import (
    CreateHousekeepingRequestSerializer,
    HousekeepingRequestSerializer,
    HousekeepingServiceSerializer,
)
from .services import (
    create_housekeeping_request,
    get_housekeeping_services,
)


class GuestHousekeepingServicesView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def get(self, request, token):
        lookup = RoomLookupSerializer(
            data={
                "token": token,
            }
        )

        lookup.is_valid(
            raise_exception=True,
        )

        services = get_housekeeping_services()

        serializer = HousekeepingServiceSerializer(
            services,
            many=True,
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )


class GuestCreateHousekeepingRequestView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request, token):
        lookup = RoomLookupSerializer(
            data={
                "token": token,
            }
        )

        lookup.is_valid(
            raise_exception=True,
        )

        room = lookup.context["room"]

        serializer = CreateHousekeepingRequestSerializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        hk_request = create_housekeeping_request(
            room=room,
            validated_data=serializer.validated_data,  # type: ignore
        )

        response_serializer = HousekeepingRequestSerializer(
            hk_request,
        )

        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED,
        )
