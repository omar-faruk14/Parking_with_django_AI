# Generated by Django 4.2.1 on 2023-06-13 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_parking_app1', '0003_vehicleentry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicleentry',
            old_name='vehicle_name',
            new_name='vehicle_registration_Name',
        ),
    ]
