# Generated by Django 5.1 on 2024-10-02 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roomapi', '0003_alter_roomparameters_room'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='device_id',
            new_name='mac_address',
        ),
    ]
