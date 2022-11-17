from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import CustomUserManager
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):

    name = models.CharField('Nome', max_length = 255)
    email = models.EmailField('E-mail', unique = True, 
                error_messages={'unique' : "E-mail já cadastrado!"}
            )

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email or self.name
