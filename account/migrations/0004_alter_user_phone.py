# Generated by Django 3.2.16 on 2023-08-17 11:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '01*********'. Up to 11 digits allowed.", regex='^\\+?1?\\d{1,11}$')]),
        ),
    ]
