from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    premium = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Konta użytkowników'
        verbose_name_plural = 'Konta użytkowników'