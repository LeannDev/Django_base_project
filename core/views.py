from django.views import View
from django.shortcuts import render
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.conf import settings

from django.views.generic import TemplateView # for urls.py

class HomeView(View):

    def get(self, request, *args, **kwargs):

        context = {
            'brand': settings.BRAND,
            'slogan': settings.SLOGAN,
            'site': settings.CURRENT_SITE,
            'slug': reverse('home'),
            'title': 'SEO meta title',
            'meta_description': 'Seo meta description',
            'social_title': "social title",
            'social_description': 'social meta_description',
            'image': '/media/main/brand.webp',
        }

        return render(request, 'home.html', context)
    
class AboutUsView(View):

    def get(self, request):

        context = {
            'brand': settings.BRAND,
            'slogan': settings.SLOGAN,
            'site': settings.CURRENT_SITE,
            'slug': reverse('about-us'),
            'title': 'SEO meta title',
            'meta_description': 'Seo meta description',
            'social_title': "social title",
            'social_description': 'social meta_description',
            'image': '/media/main/brand.webp',
        }

        return render(request, 'about_us.html', context)
    
class CookiesView(View):

    def get(self, request):

        context = {
            'brand': settings.BRAND,
            'slogan': settings.SLOGAN,
            'site': settings.CURRENT_SITE,
            'slug': reverse('cookies'),
            'title': 'SEO meta title',
            'meta_description': 'Seo meta description',
            'social_title': "social title",
            'social_description': 'social meta_description',
            'image': '/media/main/brand.webp',
        }

        return render(request, 'politics/cookies.html', context)
    
class LegalView(View):

    def get(self, request):

        context = {
            'brand': settings.BRAND,
            'slogan': settings.SLOGAN,
            'site': settings.CURRENT_SITE,
            'slug': reverse('legal'),
            'title': 'SEO meta title',
            'meta_description': 'Seo meta description',
            'social_title': "social title",
            'social_description': 'social meta_description',
            'image': '/media/main/brand.webp',
        }

        return render(request, 'politics/legal.html', context)
    
class PrivacyView(View):

    def get(self, request):

        context = {
            'brand': settings.BRAND,
            'slogan': settings.SLOGAN,
            'site': settings.CURRENT_SITE,
            'slug': reverse('privacy'),
            'title': 'SEO meta title',
            'meta_description': 'Seo meta description',
            'social_title': "social title",
            'social_description': 'social meta_description',
            'image': '/media/main/brand.webp',
        }

        return render(request, 'politics/privacy.html', context)
    

class SitemapView(Sitemap):

    changefreq = "daily"
    priority = 0.5

    def items(self):
        # Lista de nombres de vistas
        return ['home', 'about-us', 'cookies', 'legal', 'privacy']

    def location(self, item):
        return reverse(item)