# Generated by Django 4.0.5 on 2022-06-29 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Фильм')),
                ('price', models.IntegerField(verbose_name='Стоимость просмотра')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Отель')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.city', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Отель',
                'verbose_name_plural': ('Отели',),
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Тариф')),
                ('price', models.IntegerField(verbose_name='Цена (руб./мин.)')),
                ('movie1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bonus_mov1', to='billing.film', verbose_name='Бонус1')),
                ('movie2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bonus_mov2', to='billing.film', verbose_name='Бонус2')),
            ],
            options={
                'verbose_name': 'Тариф',
                'verbose_name_plural': 'Тарифы',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Категория номера')),
            ],
            options={
                'verbose_name': 'Категория номера',
                'verbose_name_plural': 'Категории номера',
            },
        ),
        migrations.CreateModel(
            name='RoomDeposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField(verbose_name='Баланс')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.room', verbose_name='Категория номера')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='deposit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.roomdeposit', verbose_name='БалансТВ'),
        ),
        migrations.AddField(
            model_name='room',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.hotel', verbose_name='Отель'),
        ),
        migrations.AddField(
            model_name='room',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.plan', verbose_name='Тариф включен'),
        ),
    ]
