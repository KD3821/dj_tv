# Generated by Django 4.0.5 on 2022-06-29 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0003_remove_roomdeposit_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomdeposit',
            name='name',
            field=models.CharField(default='Стандарт 500', max_length=50, verbose_name='Услуга'),
        ),
    ]
