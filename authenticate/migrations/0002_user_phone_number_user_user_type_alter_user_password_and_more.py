# Generated by Django 5.1.6 on 2025-02-25 09:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default=1111111111, max_length=10, validators=[django.core.validators.RegexValidator(code='nomatch', message='Phone number must be exactly 10 digits.', regex='^\\d{10}$')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('admin', 'Admin'), ('manager', 'Manager'), ('user', 'User')], default='User', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(8)]),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
