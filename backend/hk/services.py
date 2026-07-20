from django.db import transaction

from hk.exceptions import (
    InvalidHousekeepingServiceError,
)
from hk.models import (
    HousekeepingRequest,
    HousekeepingRequestItem,
    HousekeepingService,
)
from rooms.public.services import (
    get_room_by_token,
)


def get_services_by_codes(
    codes: list[str],
):
    """
    Return active housekeeping services.

    Raise InvalidHousekeepingServiceError
    if any supplied code is invalid.
    """

    services = list(
        HousekeepingService.objects.filter(
            code__in=codes,
            is_active=True,
        )
    )

    if len(services) != len(set(codes)):
        raise InvalidHousekeepingServiceError("One or more services are invalid.")

    return services


def create_request(
    *,
    room,
    note: str,
):
    return HousekeepingRequest.objects.create(
        room=room,
        note=note,
    )


def create_request_items(
    *,
    request,
    services,
):
    items = [
        HousekeepingRequestItem(
            request=request,
            service=service,
        )
        for service in services
    ]

    HousekeepingRequestItem.objects.bulk_create(
        items,
    )


def create_housekeeping_request(
    *,
    token: str,
    services: list[str],
    note: str,
):
    """
    Main business workflow.
    """

    room = get_room_by_token(token)

    service_objects = get_services_by_codes(
        services,
    )

    with transaction.atomic():
        request = create_request(
            room=room,
            note=note,
        )

        create_request_items(
            request=request,
            services=service_objects,
        )

    return request
