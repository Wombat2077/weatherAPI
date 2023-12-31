# Generated by Django 4.2.2 on 2023-06-15 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(verbose_name='latitude')),
                ('longitude', models.FloatField(verbose_name='longitude')),
            ],
        ),
        migrations.CreateModel(
            name='Precipitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prec_type', models.PositiveSmallIntegerField(verbose_name='type')),
                ('prec_strength', models.FloatField(default=0, verbose_name='strength')),
                ('cloudness', models.FloatField(default=0, verbose_name='cloudness')),
            ],
        ),
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField(verbose_name='temp')),
                ('feels', models.FloatField(verbose_name='feels_like')),
                ('water_temp', models.FloatField(verbose_name='water_temp')),
            ],
        ),
        migrations.CreateModel(
            name='Wind',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speed', models.FloatField(default=0, verbose_name='speed')),
                ('direction', models.CharField(default='c', max_length=2, verbose_name='direction')),
                ('gust', models.FloatField(default=0, verbose_name='gust')),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weather_condition', models.CharField(max_length=30, verbose_name='condition')),
                ('date', models.DateField(verbose_name='date')),
                ('prec', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='API.precipitation')),
                ('temp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='API.temperature')),
                ('wind', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='API.wind')),
            ],
        ),
    ]
