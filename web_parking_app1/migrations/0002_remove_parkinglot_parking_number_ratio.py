# Generated by Django 4.2.1 on 2023-06-04 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_parking_app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parkinglot',
            name='parking_number_ratio',
        ),
    ]
