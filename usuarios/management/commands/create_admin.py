from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Creates the default admin superuser if it does not already exist."

    def handle(self, *args, **options):
        User = get_user_model()

        email = "admin@atelier.edu"
        username = "admin"
        password = "admin12345"

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(
                    f'Superuser "{username}" already exists — skipping creation.'
                )
            )
            return

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
            # Custom required field on the Usuario model
            identificacion="0000000000",
            rol="ADMIN",
        )

        self.stdout.write(
            self.style.SUCCESS(
                f'Superuser "{username}" ({email}) created successfully.'
            )
        )
