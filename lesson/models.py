from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название', help_text='Название урока')
    description = models.TextField(verbose_name='Описание', help_text='Введите описание')
    preview = models.ImageField(upload_to='lesson/', verbose_name='Превью', help_text='Загрузите превью', **NULLABLE)
    url = models.URLField(verbose_name='Ссылка на видео', help_text='Приложите ссылку на видео урока', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('id', )
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
