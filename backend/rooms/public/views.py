# backend/rooms/public/views.py
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    RoomLookupSerializer,
    RoomSerializer,
)


class GuestRoomView(APIView):
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

        room = lookup.context["room"]

        serializer = RoomSerializer(room)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )
