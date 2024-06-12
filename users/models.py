from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    about = models.TextField(blank=True)

    def __str__(self) -> str:
        return super().__str__()
    