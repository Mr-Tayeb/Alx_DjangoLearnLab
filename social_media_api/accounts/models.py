from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUserModel(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='images/', blank=True)
    followers = models.ManyToManyField('CustomUserModel', symmetrical=False)

