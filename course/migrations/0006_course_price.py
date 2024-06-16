# Generated by Django 5.0.6 on 2024-06-09 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_course_owner_alter_course_lessons'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.PositiveIntegerField(default=1000, help_text='Укажите стоимость курса', verbose_name='Стоимость курса'),
        ),
    ]
