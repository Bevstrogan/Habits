from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            User.objects.get(email='admin@example.com').delete()
        except User.DoesNotExist:
            pass
        user = User.objects.create(
            email='admin@example.com',
            first_name='Admin',
            last_name='Example',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )
        user.set_password('123')
        user.save()