# Generated by Django 3.2.5 on 2021-09-29 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carlisting', '0009_carimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='car_images',
        ),
    ]
