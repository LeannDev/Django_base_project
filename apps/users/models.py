from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.core.validators import FileExtensionValidator

from apps.images.utils import profile_image_upload_to


class UserManager(BaseUserManager):
    # def create_user(self, username, email=None, password=None, **extra_fields):
    #     if not username:
    #         raise ValueError('Username is required')
    #     if not email:
    #         raise ValueError('Email is required')

    #     email = self.normalize_email(email)
    #     user = self.model(username=username, email=email, **extra_fields)
    #     user.set_password(password)from PIL import Image
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
    email_verified = models.BooleanField(default=False)

    objects = UserManager()

    REQUIRED_FIELDS = ['email']  # Si usás email como único campo requerido
    USERNAME_FIELD = 'username'  # Si querés seguir usando username para login

    def __str__(self):
        return f'User: {self.username}'
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to=profile_image_upload_to, blank=True, null=True, validators=[FileExtensionValidator(['jpg','png','webp','gif','jpeg'],'Only image files are allowed.')])

    def save(self, *args, **kwargs):
        if self.profile_picture:
            # Elimina la imagen anterior si existe
            try:
                old = Profile.objects.get(pk=self.pk)
                if old.profile_picture and old.profile_picture.name != self.profile_picture.name:
                    old.profile_picture.delete(save=False)
            except Profile.DoesNotExist:
                pass  # El perfil es nuevo

            # Procesar imagen
            img = Image.open(self.profile_picture)
            
            if img.mode != 'RGB':
                img = img.convert('RGB')

            width, height = img.size
            min_dim = min(width, height)
            left = (width - min_dim) / 2
            top = (height - min_dim) / 2
            right = (width + min_dim) / 2
            bottom = (height + min_dim) / 2
            img = img.crop((left, top, right, bottom)).resize((250, 250))

            buffer = BytesIO()
            img.save(buffer, format='WEBP', quality=85)
            buffer.seek(0)

            file_name = profile_image_upload_to(self, 'img.webp').split('/')[-1]
            self.profile_picture.save(file_name, ContentFile(buffer.read()), save=False)

        super().save(*args, **kwargs)

    def __str__(self):
        return f'Profile of {self.user.username}'
