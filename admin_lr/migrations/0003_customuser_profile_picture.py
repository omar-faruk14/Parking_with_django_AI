# Generated by Django 4.2.1 on 2023-06-12 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_lr', '0002_customuser_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures'),
        ),
    ]
