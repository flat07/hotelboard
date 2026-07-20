from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    CreateHousekeepingRequestSerializer,
)
from .services import (
    create_housekeeping_request,
)


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
