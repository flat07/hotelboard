from django.core.management.base import BaseCommand

from common.seeders.eng import seed_eng_requests, seed_eng_services
from common.seeders.hk import seed_hk, seed_hk_requests
from common.seeders.menu import seed_menu
from common.seeders.order import seed_order
from common.seeders.room import seed_rooms
from common.seeders.staff import seed_staff


class Command(BaseCommand):
    help = "Seed the database"

    def handle(self, *args, **options):
        seeders = [
            seed_staff,
            seed_rooms,
            seed_menu,
            seed_order,
            seed_hk,
            seed_hk_requests,
            seed_eng_services,
            seed_eng_requests,
        ]

        for seeder in seeders:
            seeder(self)

        self.stdout.write(self.style.SUCCESS("Database seeded successfully."))
