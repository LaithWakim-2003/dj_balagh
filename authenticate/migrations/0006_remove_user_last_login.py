# Generated by Django 5.1.6 on 2025-02-25 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0005_remove_user_is_active_remove_user_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
    ]
