from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    dark_mode = models.BooleanField(default=False)
    city = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.username)
    