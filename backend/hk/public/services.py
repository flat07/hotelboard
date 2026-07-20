from django.db import transaction

from hk.models import (
    HousekeepingRequest,
    HousekeepingRequestItem,
    HousekeepingService,
)
from rooms.models import Room


def get_housekeeping_services():
    return HousekeepingService.objects.filter(
        is_active=True,
    ).order_by(
        "display_order",
        "name",
    )


@transaction.atomic
def create_housekeeping_request(
    *,
    room: Room,
    validated_data: dict,
) -> HousekeepingRequest:
    items_data = validated_data.pop("items")

    request = HousekeepingRequest.objects.create(
        room=room,
        note=validated_data.get(
            "note",
            "",
        ),
    )

    for item in items_data:
        service = HousekeepingService.objects.get(
            pk=item["service"],
            is_active=True,
        )

        HousekeepingRequestItem.objects.create(
            request=request,
            service=service,
        )

    return request
