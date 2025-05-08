import os
import hashlib
from django.conf import settings
from django.utils.text import slugify

def profile_image_upload_to(instance, filename):
    # Generate a unique path for the profile image based on the user's id
    user_identifier = str(instance.user.id)
    hashed_id = hashlib.sha256(user_identifier.encode()).hexdigest()[:10]
    return f'users/{hashed_id}/profile/{instance.user.username.lower()}_{slugify(settings.BRAND)}.webp'