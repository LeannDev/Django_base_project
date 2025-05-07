import logging
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.urls import reverse
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.http import HttpResponse
from django.contrib.auth import login, get_user_model

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
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return HttpResponse('Activation link is invalid!')