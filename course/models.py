from django.db import models

from lesson.models import Lesson

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название', help_text='Название курса')
    preview = models.ImageField(upload_to='course/', verbose_name='Превью', help_text='Загрузите превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание', help_text='Введите описание')
    lessons = models.ManyToManyField(Lesson, verbose_name='Уроки', help_text='Выберите уроки', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('id', )
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
