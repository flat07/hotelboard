from hk.models import (
    HousekeepingRequest,
    HousekeepingRequestItem,
    HousekeepingService,
)
from rooms.models import Room
from staff.models import User


def seed_hk(command):
    services = [
        {
            "code": "CLEAN_ROOM",
            "name": "Clean Room",
            "display_order": 1,
        },
        {
            "code": "CHANGE_TOWELS",
            "name": "Change Towels",
            "display_order": 2,
        },
        {
            "code": "REFILL_WATER",
            "name": "Refill Water",
            "display_order": 3,
        },
        {
            "code": "EXTRA_PILLOW",
            "name": "Extra Pillow",
            "display_order": 4,
        },
    ]

    for service in services:
        HousekeepingService.objects.update_or_create(
            code=service["code"],
            defaults={
                "name": service["name"],
                "display_order": service["display_order"],
                "is_active": True,
            },
        )

    command.stdout.write(
        command.style.SUCCESS("✓ Housekeeping services seeded successfully.")
    )


def seed_hk_requests(command):
    HousekeepingRequest.objects.all().delete()

    staff = User.objects.get(
        username="housekeeping",
    )

    requests = [
        {
            "room": "101",
            "status": HousekeepingRequest.Status.PENDING,
            "assigned_to": None,
            "note": "Please clean after 2 PM.",
            "services": [
                "CLEAN_ROOM",
                "CHANGE_TOWELS",
            ],
        },
        {
            "room": "102",
            "status": HousekeepingRequest.Status.ASSIGNED,
            "assigned_to": staff,
            "note": "Need extra towels.",
            "services": [
                "CHANGE_TOWELS",
                "EXTRA_PILLOW",
            ],
        },
        {
            "room": "201",
            "status": HousekeepingRequest.Status.COMPLETED,
            "assigned_to": staff,
            "note": "",
            "services": [
                "REFILL_WATER",
                "CLEAN_ROOM",
            ],
        },
    ]

    for data in requests:
        room = Room.objects.get(
            room_number=data["room"],
        )

        request = HousekeepingRequest.objects.create(
            room=room,
            assigned_to=data["assigned_to"],
            status=data["status"],
            note=data["note"],
        )

        for code in data["services"]:
            service = HousekeepingService.objects.get(
                code=code,
            )

            HousekeepingRequestItem.objects.create(
                request=request,
                service=service,
            )

    command.stdout.write(
        command.style.SUCCESS("✓ Housekeeping requests seeded successfully.")
    )
