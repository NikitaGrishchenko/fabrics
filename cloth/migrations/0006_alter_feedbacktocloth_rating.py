# Generated by Django 4.0.4 on 2022-05-14 17:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloth', '0005_feedbacktocloth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbacktocloth',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)], verbose_name='Рейтинг'),
        ),
    ]