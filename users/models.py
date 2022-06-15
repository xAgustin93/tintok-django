import os
from django.db import models
from django.contrib.auth.models import AbstractUser


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.id, ext)
    return os.path.join('avatar/', filename)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to=get_file_path, blank=True)
    description = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=100, blank=True)
    instagram = models.CharField(max_length=100, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
