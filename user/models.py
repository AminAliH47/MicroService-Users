from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom user model
    """

    def save(self, *args, **kwargs):
        # Hash user password before save in Database
        self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)
