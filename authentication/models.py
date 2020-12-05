from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    premium = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    zip_code = models.CharField(max_length=100, blank=True, null=True)
    telephone = models.IntegerField(max_length=100, blank=True, null=True)
    business = models.IntegerField(max_length=100, blank=True, null=True)
    tax_id = models.IntegerField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Konta użytkowników'
        verbose_name_plural = 'Konta użytkowników'