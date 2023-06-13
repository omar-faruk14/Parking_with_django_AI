# Generated by Django 4.2.1 on 2023-06-13 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_parking_app1', '0002_remove_parkinglot_parking_number_ratio'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_name', models.CharField(max_length=255)),
                ('entry_time', models.DateTimeField(auto_now_add=True)),
                ('exit_time', models.DateTimeField(blank=True, null=True)),
                ('parking_lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_parking_app1.parkinglot')),
            ],
        ),
    ]
