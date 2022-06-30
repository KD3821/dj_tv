from django.contrib import admin
from django.urls import path, include
from billing.views import list_view, home_view, edit_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', list_view, name='list'),
    path('edit/', edit_view, name='edit'),
    path('', home_view, name='home'),
    path('accounts/', include(('accounts.urls', 'account.views'), 'accounts')),
]
