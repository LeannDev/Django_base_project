from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()

def validate_unique_username(value):
    if User.objects.filter(username__iexact=value).exists():
        raise ValidationError("This username is already taken. Please choose a different one.")