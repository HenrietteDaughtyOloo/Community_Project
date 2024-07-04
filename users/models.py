from django.db import models
from django.contrib.auth.models import AbstractUser
# from signal_protocol import SignalClient
# from signal_protocol import curve, identity_key, state, storage

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

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=ADMIN)
    # signal_identity_key = models.TextField()
    # signal_pre_keys = models.TextField()
    # signal_signed_pre_key = models.TextField()



    def __str__(self) -> str:
        return super().__str__()
    
    # def generate_signal_keys(self):
    #     client = SignalClient()
    #     self.identity_key_pair = identity_key.IdentityKeyPair.generate()
    #     self.pre_key_pair = curve.KeyPair.generate()
    #     self.signal_signed_pre_key = client.generate_signed_pre_key(client.generate_identity_key_pair()).serialize()
    #     self.save()