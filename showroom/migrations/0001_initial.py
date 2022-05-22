# Generated by Django 4.0.4 on 2022-05-22 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClothShowroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('image', models.ImageField(upload_to='', verbose_name='Фото')),
                ('description', models.CharField(blank=True, max_length=350, null=True, verbose_name='Описание')),
                ('isConfirmed', models.BooleanField(default=False, verbose_name='Опубликовать?')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Шоурум',
                'verbose_name_plural': 'Шоурум',
            },
        ),
    ]