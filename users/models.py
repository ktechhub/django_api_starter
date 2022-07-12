import time
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

def image_directory(instance, filename):
    return '/'.join(['images', 'avatar', f"{str(time.time())}_{instance.name}_{str(filename)}"])

class CustomUser(AbstractUser):
    username = models.CharField(max_length=120, blank=True, null=True, unique=True)
    name = models.CharField(max_length=120, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)
    avatar = models.ImageField(blank=True, null=True, upload_to=image_directory, default="avatar.png")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()

    class Meta:
        verbose_name_plural = "Users"

    def __str__(self):
        return self.name.capitalize() if self.name else self.email

