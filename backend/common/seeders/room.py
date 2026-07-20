from rooms.models import Room


def seed_rooms(command):
    rooms = [
        {
            "room_number": "101",
            "floor": 1,
            "room_type": Room.RoomType.STANDARD,
            "public_token": "room-101-test-token",
        },
        {
            "room_number": "102",
            "floor": 1,
            "room_type": Room.RoomType.STANDARD,
        },
        {
            "room_number": "103",
            "floor": 1,
            "room_type": Room.RoomType.DELUXE,
        },
        {
            "room_number": "104",
            "floor": 1,
            "room_type": Room.RoomType.SUITE,
        },
        {
            "room_number": "201",
            "floor": 2,
            "room_type": Room.RoomType.STANDARD,
        },
        {
            "room_number": "202",
            "floor": 2,
            "room_type": Room.RoomType.STANDARD,
        },
        {
            "room_number": "203",
            "floor": 2,
            "room_type": Room.RoomType.DELUXE,
        },
        {
            "room_number": "204",
            "floor": 2,
            "room_type": Room.RoomType.SUITE,
        },
        {
            "room_number": "301",
            "floor": 3,
            "room_type": Room.RoomType.STANDARD,
        },
        {
            "room_number": "302",
            "floor": 3,
            "room_type": Room.RoomType.DELUXE,
        },
        {
            "room_number": "303",
            "floor": 3,
            "room_type": Room.RoomType.DELUXE,
        },
        {
            "room_number": "304",
            "floor": 3,
            "room_type": Room.RoomType.SUITE,
        },
    ]

    for room in rooms:
        defaults = {
            "floor": room["floor"],
            "room_type": room["room_type"],
            "is_active": True,
        }

        if "public_token" in room:
            defaults["public_token"] = room["public_token"]

        Room.objects.get_or_create(
            room_number=room["room_number"],
            defaults=defaults,
        )

    command.stdout.write(command.style.SUCCESS("✓ Rooms seeded successfully."))
