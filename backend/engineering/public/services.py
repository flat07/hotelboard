from django.db import transaction

from engineering.models import (
    EngineeringRequest,
    EngineeringRequestItem,
    EngineeringService,
)
from rooms.models import Room


def get_engineering_services():
    return EngineeringService.objects.filter(
        is_active=True,
    ).order_by(
        "display_order",
        "name",
    )


@transaction.atomic
def create_engineering_request(
    *,
    room: Room,
    validated_data: dict,
) -> EngineeringRequest:
    items_data = validated_data.pop("items")

    request = EngineeringRequest.objects.create(
        room=room,
        note=validated_data.get(
            "note",
            "",
        ),
    )

    for item in items_data:
        service = EngineeringService.objects.get(
            pk=item["service"],
            is_active=True,
        )

        EngineeringRequestItem.objects.create(
            request=request,
            service=service,
        )

    return request
