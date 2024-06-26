from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    about = models.TextField(blank=True)
    phone_number = models.IntegerField(blank=True)
    ADMIN = 'admin'
    MEMBER = 'member'

    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (MEMBER, 'Member'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=MEMBER)


    def __str__(self) -> str:
        return super().__str__()