# Generated by Django 5.1.6 on 2025-02-25 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0004_remove_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
    ]
