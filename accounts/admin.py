from django.contrib import admin
from .models import ManagerHotel

@admin.register(ManagerHotel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'timestamp', 'admin', 'staff', 'is_active', 'city', 'hotel']
    list_filter = ['city', 'hotel']
    fieldsets = [(None, {'fields': ('email', 'password')}),
                 ('Permissions', {'fields': ('admin', 'staff')}),
                 ('Settings', {'fields': ('city', 'hotel')})
                 ]
