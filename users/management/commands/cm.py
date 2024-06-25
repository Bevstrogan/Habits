from django.contrib.auth.models import Group
from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            Group.objects.get(name="Модератор").delete()
        except Group.DoesNotExist:
            pass
        moderator = Group.objects.create(name="Модератор")
        moderator.save()
        try:
            User.objects.get(email='moderator@example.com').delete()
        except User.DoesNotExist:
            pass
        user = User.objects.create(
            email='moderator@example.com',
            first_name='Moderator',
            last_name='Example',
            is_staff=True,
            is_active=True,
        )
        user.groups.set([moderator.pk])
        user.set_password('123')
        user.save()
