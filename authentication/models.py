from django.db import models
from django.contrib.auth.models import AbstractUser

class Author(AbstractUser):
    bio = models.TextField()
    subtitle = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='author_images/', blank=True, null=True)
    password_enabled = models.BooleanField(default=True)
