# backend/room_service/public/views.py
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from rooms.public.serializers import RoomLookupSerializer

from .serializers import (
    CreateOrderSerializer,
    MenuCategorySerializer,
    RoomServiceOrderSerializer,
)
from .services import (
    create_room_service_order,
    get_menu_categories,
)


class GuestMenuView(APIView):
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

        categories = get_menu_categories()

        serializer = MenuCategorySerializer(
            categories,
            many=True,
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )


class GuestCreateOrderView(APIView):
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

        serializer = CreateOrderSerializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        order = create_room_service_order(
            room=room,
            validated_data=serializer.validated_data,  # type: ignore
        )

        response_serializer = RoomServiceOrderSerializer(
            order,
        )

        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED,
        )
