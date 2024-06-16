from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from users.models import User


class Command(BaseCommand):
    help = 'Создание суперпользователя'

    def handle(self, *args, **options):
        try:
            user = User.objects.create(
                email='admin',
                is_staff=True,
                is_superuser=True,
                is_active=True
            )
            user.set_password('12345')
            user.save()
            self.stdout.write('Суперпользователь создан !')
        except IntegrityError:
            self.stdout.write('Суперпользователь с такой почтой уже был создан !')
