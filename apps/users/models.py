from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    # def create_user(self, username, email=None, password=None, **extra_fields):
    #     if not username:
    #         raise ValueError('Username is required')
    #     if not email:
    #         raise ValueError('Email is required')

    #     email = self.normalize_email(email)
    #     user = self.model(username=username, email=email, **extra_fields)
    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user

    # If superuser is not required email activation.
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser requires is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser requires is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)

    objects = UserManager()

    REQUIRED_FIELDS = ['email']  # Si usás email como único campo requerido
    USERNAME_FIELD = 'username'  # Si querés seguir usando username para login

    def __str__(self):
        return f'User: {self.username}'
