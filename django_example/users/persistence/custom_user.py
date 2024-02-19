from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=False)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    bio = models.CharField(max_length=255, blank=True)
