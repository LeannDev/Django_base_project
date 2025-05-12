from PIL import Image
from io import BytesIO
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.core.files.base import ContentFile

from apps.images.utils import profile_image_upload_to

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to=profile_image_upload_to, blank=True, null=True, validators=[FileExtensionValidator(['jpg','png','webp','gif','jpeg'],'Only image files are allowed.')])

    def save(self, *args, **kwargs):
        if self.profile_picture:
            # Check if the image is a new one
            # If the image is not new, delete the old one
            try:
                old = Profile.objects.get(pk=self.pk)
                if old.profile_picture and old.profile_picture.name != self.profile_picture.name:
                    old.profile_picture.delete(save=False)
            except Profile.DoesNotExist:
                pass  # profile is new, no need to delete old image

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