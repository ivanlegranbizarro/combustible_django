from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .manager import CustomUserManager


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(_("Nombre de usuario"), max_length=50)
    first_name = models.CharField(_("Tu nombre"), max_length=100)
    last_name = models.CharField(_("Tu apellido"), max_length=100)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name"]

    def __str__(self):
        return self.email
