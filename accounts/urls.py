from django.urls import path
from .views import login_view, logout_view, register_view, update_view, delete_view, contact_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('register_ok/', register_view, name='register_done'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('update/', update_view, name='update'),
    path('delete/', delete_view, name='delete'),
    path('contact/', contact_view, name='contact'),
]