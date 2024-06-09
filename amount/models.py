from django.db import models

from course.models import Course


class Amount(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', help_text='Выберите курс')
    amount = models.PositiveIntegerField(verbose_name='Сумма оплаты')
    session_id = models.CharField(max_length=256, blank=True, null=True, verbose_name='id сессии')
    link = models.URLField(max_length=512, blank=True, null=True, verbose_name='Ссылка на оплату')

    def __str__(self):
        return f'{self.course}: {self.amount}'

    class Meta:
        ordering = ('id', )
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'
