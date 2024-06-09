from django.conf import settings
from django.db import models

from course.models import Course

NULLABLE = {'blank': True, 'null': True}


class Amount(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', help_text='Выберите курс')
    amount = models.PositiveIntegerField(verbose_name='Сумма оплаты')
    session_id = models.CharField(max_length=256, **NULLABLE, verbose_name='id сессии')
    link = models.URLField(max_length=512, **NULLABLE, verbose_name='Ссылка на оплату')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name='Пользователь',
        **NULLABLE
    )

    def __str__(self):
        return f'{self.course}: {self.amount}'

    class Meta:
        ordering = ('id', )
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'
