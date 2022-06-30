from django.contrib import admin
from .models import City, Hotel, Room, Plan, Film, RoomDeposit

admin.site.register(City)

@admin.register(Film)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_filter = ['price']


@admin.register(Hotel)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'city']
    list_filter = ['city']


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'movie', 'hotel']
    list_filter = ['price', 'hotel']


@admin.register(Room)
class DepositAdmin(admin.ModelAdmin):
    list_display = ['name', 'plan', 'deposit', 'film', 'hotel']
    list_filter = ['hotel']

@admin.register(RoomDeposit)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'balance']
    list_filter = ['name']