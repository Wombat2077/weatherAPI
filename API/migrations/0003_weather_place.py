# Generated by Django 4.2.2 on 2023-06-15 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_place_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather',
            name='place',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='API.place'),
        ),
    ]
