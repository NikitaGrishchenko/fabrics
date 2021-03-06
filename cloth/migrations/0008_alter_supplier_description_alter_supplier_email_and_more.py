# Generated by Django 4.0.4 on 2022-05-17 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloth', '0007_supplier_date_of_foundation_supplier_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='description',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Логотип'),
        ),
    ]
