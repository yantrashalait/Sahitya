from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_publication = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="profile", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_profile')
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username + '-' + 'Profile'

