# Generated by Django 4.1.5 on 2023-02-24 12:44

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_managers"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[("objects", django.contrib.auth.models.UserManager()),],
        ),
    ]
