from celery import shared_task
from datetime import timedelta
from django.utils import timezone

from .models import User


@shared_task
def check_users():
    """Проверяет активность пользователя и если об был неактивен 30 дней, то блокирует его."""

    users = User.objects.filter(is_superuser=False)
    for user in users:
        user_date = user.date_joined if user.last_login is None else user.last_login
        result = timezone.now() - user_date
        if result >= timedelta(days=30):
            user.is_active = False
            user.save()
