# Generated by Django 4.0.4 on 2024-01-21 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_attendance_presence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='presence',
        ),
    ]
