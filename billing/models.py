from django.db import models
from django.db.models import CharField, IntegerField


class City(models.Model):
    name = CharField(max_length=50, verbose_name='Город', unique=True)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = CharField(max_length=50, verbose_name='Отель', unique=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город')

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'

    def __str__(self):
        return self.name


class Room(models.Model):
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE, verbose_name='Отель', default='1')
    name = CharField(max_length=50, verbose_name='Категория номера', unique=True)
    plan = models.ForeignKey('Plan', on_delete=models.CASCADE, verbose_name='Тариф включен')
    deposit = models.ForeignKey('RoomDeposit', on_delete=models.CASCADE, verbose_name='Баланс ТВ')
    film = models.ForeignKey('Film', on_delete=models.CASCADE, verbose_name='Фильм включен', default='1')

    class Meta:
        verbose_name = 'Категория номера'
        verbose_name_plural = 'Категории номера'

    def __str__(self):
        return self.name


class Plan(models.Model):
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE, verbose_name='Название отеля', default='1')
    name = CharField(max_length=50, verbose_name='Тариф', unique=True)
    price = IntegerField(verbose_name='Цена (руб./мин.)')
    movie = models.ForeignKey('Film', on_delete=models.CASCADE, verbose_name='Бонус')


    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'

    def __str__(self):
        return self.name


class Film(models.Model):
    name = CharField(max_length=50, verbose_name='Фильм', unique=True)
    price = IntegerField(verbose_name='Стоимость просмотра')


    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.name


class RoomDeposit(models.Model):
    name = CharField(max_length=50, verbose_name='Депозит номера', default='Стандарт 500')
    balance = IntegerField(verbose_name='Баланс')

    class Meta:
        verbose_name = 'Депозит номера'
        verbose_name_plural = 'Депозиты'

    def __str__(self):
        return self.name