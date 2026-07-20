from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from rooms.public.serializers import RoomLookupSerializer

from .serializers import (
    CreateEngineeringRequestSerializer,
    EngineeringRequestSerializer,
    EngineeringServiceSerializer,
)
from .services import (
    create_engineering_request,
    get_engineering_services,
)


class GuestEngineeringServicesView(APIView):
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

        services = get_engineering_services()

        serializer = EngineeringServiceSerializer(
            services,
            many=True,
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )


class GuestCreateEngineeringRequestView(APIView):
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

        serializer = CreateEngineeringRequestSerializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        engineering_request = create_engineering_request(
            room=room,
            validated_data=serializer.validated_data,  # type: ignore
        )

        response_serializer = EngineeringRequestSerializer(
            engineering_request,
        )

        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED,
        )
