# Generated by Django 4.2.1 on 2023-06-13 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_parking_app1', '0004_rename_vehicle_name_vehicleentry_vehicle_registration_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleentry',
            name='vehicle_registration_Name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
