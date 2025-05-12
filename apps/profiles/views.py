from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.urls import reverse
from django.conf import settings

from .models import Profile
from .forms import ProfileForm

class ProfileEditView(LoginRequiredMixin, UpdateView):
    template_name = 'profile_edit.html'
    form_class = ProfileForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand'] = settings.BRAND
        context['slogan'] = settings.SLOGAN
        context['site'] = settings.CURRENT_SITE
        context['slug'] = reverse('profile_edit')
        context['title'] = 'Edit Profile'
        context['meta_description'] = 'Edit Profile'
        context['social_title'] = 'Edit Profile'
        context['social_description'] = 'Edit Profile'
        context['image'] = '/media/main/brand.webp'
        
        return context

    def get_object(self):
        return Profile.objects.get_or_create(user=self.request.user)[0]
    
class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'
    slug_field = 'user__username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand'] = settings.BRAND
        context['slogan'] = settings.SLOGAN
        context['site'] = settings.CURRENT_SITE
        context['title'] = f'Profile of {self.kwargs["username"]}'
        context['meta_description'] = 'Profile'
        context['social_title'] = 'Profile'
        context['social_description'] = 'Profile'
        context['image'] = '/media/main/brand.webp'
        
        return context

    def get_queryset(self):
        return Profile.objects.select_related('user').filter(user__is_active=True)