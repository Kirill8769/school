# Generated by Django 5.0.6 on 2024-05-20 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Название курса', max_length=150, verbose_name='Название')),
                ('preview', models.ImageField(blank=True, help_text='Загрузите превью', null=True, upload_to='course/', verbose_name='Превью')),
                ('description', models.TextField(help_text='Введите описание', verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
                'ordering': ('id',),
            },
        ),
    ]