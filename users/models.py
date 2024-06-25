from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Почта")

    phone = models.CharField(
        max_length=20, verbose_name="Номер телефона", null=True, blank=True
    )
    city = models.CharField(max_length=80, verbose_name="Город", null=True, blank=True)
    avatar = models.ImageField(
        upload_to="users/", verbose_name="Аватар", null=True, blank=True
    )
    chat_id = models.CharField(max_length=100, verbose_name="Телеграм", null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
