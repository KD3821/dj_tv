# Generated by Django 4.0.5 on 2022-06-30 09:36

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='managerhotel',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='managerhotel',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]