# Generated by Django 4.2.2 on 2023-06-21 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_weather_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature',
            name='water_temp',
            field=models.FloatField(null=True, verbose_name='water_temp'),
        ),
    ]