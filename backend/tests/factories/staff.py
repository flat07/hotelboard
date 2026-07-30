# tests/factories/staff.py

import factory
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory

User = get_user_model()


class StaffFactory(DjangoModelFactory):
    class Meta:
        model = User
        skip_postgeneration_save = True

    username = factory.Sequence(lambda n: f"user{n}")  # type: ignore
    first_name = factory.Faker("first_name")  # type: ignore
    last_name = factory.Faker("last_name")  # type: ignore
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")  # type: ignore

    role = User.Role.HOUSEKEEPING  # type: ignore

    @factory.post_generation  # type: ignore
    def password(self, create, extracted, **kwargs):
        password = extracted or "password123"
        self.set_password(password)  # type: ignore
        if create:
            self.save()  # type: ignore
