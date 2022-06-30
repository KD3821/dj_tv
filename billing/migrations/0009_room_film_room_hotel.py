# Generated by Django 4.0.5 on 2022-06-30 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0008_alter_roomdeposit_options_alter_roomdeposit_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='film',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='billing.film', verbose_name='Фильм включен'),
        ),
        migrations.AddField(
            model_name='room',
            name='hotel',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='billing.hotel', verbose_name='Отель'),
        ),
    ]