import logging
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

logger = logging.getLogger('core')

def email_sender(subject, message, recipients, template_html=None, context=None, sender=None):
    """
    Email sender function to send emails with optional HTML templates.
    
    Args:
    - subject: Email subject (str)
    - message: Email message (str)
    - recipients: Recipients list (list of str)
    - template_html: Template HTML file (str). If None, no use HTML template
    - context: Context for the HTML template (dict). If None, no use context
    - sender: Sender email (str). If None, use DEFAULT_FROM_EMAIL from settings
    """
    
    sender = sender or settings.DEFAULT_FROM_EMAIL
    
    try:

        if template_html and context:
            html_message = render_to_string(template_html, context)
            plain_message = strip_tags(html_message)
        else:
            html_message = None
            plain_message = message
        
        # Send the email
        send_mail(
            subject=subject,
            message=plain_message,
            from_email=sender,
            recipient_list=recipients,
            html_message=html_message,
            fail_silently=False
        )
        
        return True
    except Exception as e:
        logger.error(f"Error sending email: {e}")
        return False