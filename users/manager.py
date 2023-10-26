from django.contrib.auth.models import BaseUserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, username, first_name, password, **kwargs):
        now = timezone.now()
        if not email:
            raise ValueError(_("El campo email es requerido"))
        if not username:
            raise ValueError(_("El campo username es requerido"))

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            first_name=first_name,
            last_login=now,
            **kwargs,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, first_name, password, **kwargs):
        return self._create_user(email, username, first_name, password, **kwargs)

    def create_superuser(self, email, username, first_name, password, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)

        if kwargs.get("is_staff") is not True:
            raise ValueError(_("El campo is_staff debe ser verdadera"))
        if kwargs.get("is_superuser") is not True:
            raise ValueError(_("El campo is_superuser debe ser verdadero"))

        return self._create_user(email, username, first_name, password, **kwargs)
