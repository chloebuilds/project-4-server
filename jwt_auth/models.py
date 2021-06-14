from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import BooleanField

# AbstractUser gives us some nifty methods upon which to build our own User model
class User(AbstractUser):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    email = models.EmailField(_('email address'), unique = True)
    avatar = models.CharField(max_length=250)
    theme_preference = BooleanField
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)
    