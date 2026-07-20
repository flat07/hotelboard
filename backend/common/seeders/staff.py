from django.contrib.auth import get_user_model

User = get_user_model()


def seed_staff(command):
    staff_users = [
        {
            "username": "admin",
            "first_name": "admin",
            "last_name": "admin",
            "role": User.Role.MANAGER,  # type: ignore
            "is_superuser": True,
        },
        {
            "username": "manager",
            "first_name": "Hotel",
            "last_name": "Manager",
            "role": User.Role.MANAGER,  # type: ignore
            "is_superuser": True,
        },
        {
            "username": "housekeeping",
            "first_name": "John",
            "last_name": "Housekeeping",
            "role": User.Role.HOUSEKEEPING,  # type: ignore
            "is_superuser": False,
        },
        {
            "username": "engineering",
            "first_name": "Jane",
            "last_name": "Engineering",
            "role": User.Role.ENGINEERING,  # type: ignore
            "is_superuser": False,
        },
        {
            "username": "roomservice",
            "first_name": "Mike",
            "last_name": "Room Service",
            "role": User.Role.ROOM_SERVICE,  # type: ignore
            "is_superuser": False,
        },
    ]

    for staff in staff_users:
        user, created = User.objects.get_or_create(
            username=staff["username"],
            defaults={
                "first_name": staff["first_name"],
                "last_name": staff["last_name"],
                "role": staff["role"],
                "is_staff": True,
                "is_superuser": staff["is_superuser"],
            },
        )

        # Always ensure the password is set
        user.set_password("admin")
        user.save()

    command.stdout.write(command.style.SUCCESS("✓ Staff seeded successfully."))
