from django.utils import timezone

from engineering.models import (
    EngineeringRequest,
    EngineeringRequestItem,
    EngineeringService,
)
from rooms.models import Room
from staff.models import User


def seed_eng_services(command):
    services = [
        {
            "code": "AIR_CONDITIONER",
            "name": "Air Conditioner",
            "display_order": 1,
        },
        {
            "code": "LIGHTING",
            "name": "Lighting",
            "display_order": 2,
        },
        {
            "code": "TELEVISION",
            "name": "Television",
            "display_order": 3,
        },
        {
            "code": "DOOR_LOCK",
            "name": "Door Lock",
            "display_order": 4,
        },
        {
            "code": "PLUMBING",
            "name": "Plumbing",
            "display_order": 5,
        },
        {
            "code": "MINI_BAR",
            "name": "Mini Bar",
            "display_order": 6,
        },
    ]

    for service in services:
        EngineeringService.objects.update_or_create(
            code=service["code"],
            defaults={
                "name": service["name"],
                "display_order": service["display_order"],
                "is_active": True,
            },
        )

    command.stdout.write(
        command.style.SUCCESS("✓ Engineering services seeded successfully.")
    )


def seed_eng_requests(command):
    EngineeringRequest.objects.all().delete()

    engineer = User.objects.get(
        username="engineering",
    )

    requests = [
        {
            "room": "101",
            "status": EngineeringRequest.Status.PENDING,
            "assigned_to": None,
            "note": "Air conditioner is not cooling.",
            "services": [
                "AIR_CONDITIONER",
            ],
        },
        {
            "room": "102",
            "status": EngineeringRequest.Status.ASSIGNED,
            "assigned_to": engineer,
            "note": "Bathroom light is flickering.",
            "services": [
                "LIGHTING",
            ],
        },
        {
            "room": "201",
            "status": EngineeringRequest.Status.IN_PROGRESS,
            "assigned_to": engineer,
            "note": "TV has no signal.",
            "services": [
                "TELEVISION",
            ],
        },
        {
            "room": "202",
            "status": EngineeringRequest.Status.COMPLETED,
            "assigned_to": engineer,
            "note": "Door lock replaced.",
            "completed_at": timezone.now(),
            "services": [
                "DOOR_LOCK",
            ],
        },
    ]

    for data in requests:
        room = Room.objects.get(
            room_number=data["room"],
        )

        request = EngineeringRequest.objects.create(
            room=room,
            assigned_to=data["assigned_to"],
            status=data["status"],
            note=data["note"],
            completed_at=data.get("completed_at"),
        )

        for code in data["services"]:
            service = EngineeringService.objects.get(
                code=code,
            )

            EngineeringRequestItem.objects.create(
                request=request,
                service=service,
            )

    command.stdout.write(
        command.style.SUCCESS("✓ Engineering requests seeded successfully.")
    )
