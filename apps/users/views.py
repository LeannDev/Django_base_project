import logging
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login, logout
from django.urls import reverse
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.http import HttpResponse
from django.contrib.auth import login, get_user_model
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from .forms import CustomUserCreationForm

logger = logging.getLogger(__name__)
User = get_user_model()

class SignUpView(FormView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand'] = settings.BRAND
        context['slogan'] = settings.SLOGAN
        context['site'] = settings.CURRENT_SITE
        context['slug'] = reverse('signup')
        context['title'] = 'Sign Up'
        context['meta_description'] = 'Sign Up'
        context['social_title'] = 'Sign Up'
        context['social_description'] = 'Sign Up'
        context['image'] = '/media/main/brand.webp'
        return context

    def form_valid(self, form):
        user = form.save()
        logger.info(f"User {user.username} created successfully.")
        return super().form_valid(form)
    

class LoginView(LoginView):
    template_name = 'registration/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand'] = settings.BRAND
        context['slogan'] = settings.SLOGAN
        context['site'] = settings.CURRENT_SITE
        context['slug'] = reverse('login')
        context['title'] = 'Login'
        context['meta_description'] = 'Login'
        context['social_title'] = 'Login'
        context['social_description'] = 'Login'
        context['image'] = '/media/main/brand.webp'
        return context
    
def logout_view(request):
    logout(request)
    return redirect('/')

def account_activation(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        user.is_active = True
        user.email_verified = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return HttpResponse('Activation link is invalid!')
    
class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('password_change_done')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand'] = settings.BRAND
        context['slogan'] = settings.SLOGAN
        context['site'] = settings.CURRENT_SITE
        context['title'] = 'Change Password'
        context['meta_description'] = 'Change Password'
        context['social_title'] = 'Change Password'
        context['social_description'] = 'Change Password'
        context['image'] = '/media/main/brand.webp'
        return context
    
    def form_valid(self, form):
        user = form.save()
        update_session_auth_hash(self.request, user) # need to keep the user logged in after password change
        logger.info(f"Password changed successfully for user {user.username}.")
        return super().form_valid(form)
    
class CustomPasswordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand'] = settings.BRAND
        context['slogan'] = settings.SLOGAN
        context['site'] = settings.CURRENT_SITE
        context['title'] = 'Password Change Done'
        context['meta_description'] = 'Password Change Done'
        context['social_title'] = 'Password Change Done'
        context['social_description'] = 'Password Change Done'
        context['image'] = '/media/main/brand.webp'
        return context
    
class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'emails/password_reset_email.txt'  # Unformat text (fallback)
    html_email_template_name = 'emails/password_reset_email.html'  # HTML
    subject_template_name = 'emails/subjects/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand'] = settings.BRAND
        context['slogan'] = settings.SLOGAN
        context['site'] = settings.CURRENT_SITE
        context['title'] = 'Password Reset'
        context['meta_description'] = 'Password Reset'
        context['social_title'] = 'Password Reset'
        context['social_description'] = 'Password Reset'
        context['image'] = '/media/main/brand.webp'

        return context
    
    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
        """Send an email with the given subject and body."""
        subject = render_to_string(subject_template_name, context).strip()
        body = render_to_string(email_template_name, context)
        email_message = EmailMultiAlternatives(subject, body, from_email, [to_email])

        if html_email_template_name:
            html_email = render_to_string(html_email_template_name, context)
            email_message.attach_alternative(html_email, 'text/html')

        email_message.send()
        logger.info(f"Password reset email sent to {to_email}.")

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand'] = settings.BRAND
        context['slogan'] = settings.SLOGAN
        context['site'] = settings.CURRENT_SITE
        context['title'] = 'Password Reset Done'
        context['meta_description'] = 'Password Reset Done'
        context['social_title'] = 'Password Reset Done'
        context['social_description'] = 'Password Reset Done'
        context['image'] = '/media/main/brand.webp'
        return context
    
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand'] = settings.BRAND
        context['slogan'] = settings.SLOGAN
        context['site'] = settings.CURRENT_SITE
        context['title'] = 'Password Reset Confirm'
        context['meta_description'] = 'Password Reset Confirm'
        context['social_title'] = 'Password Reset Confirm'
        context['social_description'] = 'Password Reset Confirm'
        context['image'] = '/media/main/brand.webp'
        return context
    
    def form_valid(self, form):
        user = form.save()
        update_session_auth_hash(self.request, user)
        logger.info(f"Password reset successfully for user {user.username}.")
        return super().form_valid(form)
    
class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand'] = settings.BRAND
        context['slogan'] = settings.SLOGAN
        context['site'] = settings.CURRENT_SITE
        context['title'] = 'Password Reset Complete'
        context['meta_description'] = 'Password Reset Complete'
        context['social_title'] = 'Password Reset Complete'
        context['social_description'] = 'Password Reset Complete'
        context['image'] = '/media/main/brand.webp'
        
        return context