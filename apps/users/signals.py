import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth import get_user_model

from apps.emails.services import email_sender
from .models import Profile

logger = logging.getLogger(__name__)
User = get_user_model()

@receiver(post_save, sender=User)
def after_user_created(sender, instance, created, **kwargs):

    if created and not instance.is_active:
        instance.refresh_from_db()  # Refresh the instance to get the latest data
        uid = urlsafe_base64_encode(force_bytes(instance.pk))
        token = default_token_generator.make_token(instance)
        link = f"https://{settings.CURRENT_SITE}{reverse('account_activation', kwargs={'uidb64': uid, 'token': token})}"

        # Create a profile for the user
        Profile.objects.get_or_create(user=instance)

        # Send the email confirmation
        try:
            email_sender(
                subject=f"Welcome to {settings.BRAND}",
                message=f"Please confirm your email address. {link}",
                recipients=[instance.email],
                template_html="emails/welcome.html",
                context={
                    'username': instance.username,
                    'year': timezone.now().year,
                    'link': link,
                    'brand': settings.BRAND,
                }
            )
        except Exception as e:
            logger.error(f"Error sending email: {e}")