from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
async def send_course_changes(subject, message, email):
    """Отправляет письма об изменении курса подписанным на него пользователям."""

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
