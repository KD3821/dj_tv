from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models import EmailField, CharField, BooleanField, DateTimeField, ForeignKey
from django.contrib.auth.hashers import make_password, identify_hasher
from django.contrib.auth.models import UserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, name=None, full_name=None, is_active=True, is_staff=None, is_admin=None):
        """
        Create and save a user with the given  username, email, and password.
        """
        if not email:
            raise ValueError('User must have an e-mail address')
        if not password:
            raise ValueError('User must enter password')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.staff = is_staff
        user.admin = is_admin
        user.is_active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, name=None):
        user = self.create_user(email, name=name, password=password, is_staff=True, is_admin=True)
        return user

    def create_staffuser(self, email, password=None, name=None):
        user = self.create_user(email, name=name, password=password, is_staff=True, is_admin=False)
        return user



class ManagerHotel(AbstractBaseUser):
    email = EmailField(unique=True, max_length=255)
    name = CharField(max_length=255, blank=True, null=True)
    city = ForeignKey('billing.City', on_delete=models.SET_NULL, null=True, blank=True)
    hotel = ForeignKey('billing.Hotel', on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = DateTimeField(auto_now_add=True)
    staff = BooleanField(default=False)
    admin = BooleanField(default=False)
    is_active = BooleanField(default=True)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email

    def get_short_name(self):
        if self.name:
            return self.name
        return self.email

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        if self.admin:
            return True
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    def save(self, *args, **kwargs):
        try:
            _alg = identify_hasher(self.password)
        except ValueError:
            self.password = make_password(self.password)
        super().save(*args,**kwargs)