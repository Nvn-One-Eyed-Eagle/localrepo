from django.db import models
from django.contrib.auth.models import AbstractUser

class Author(AbstractUser):
    bio = models.TextField("max_length = 200")
