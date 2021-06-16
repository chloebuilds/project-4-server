from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    avatar = models.CharField(max_length=250)
    dark_mode = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.username)
    