from django.views import View
from django.shortcuts import render
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.http import JsonResponse
from django.views.generic import TemplateView # for urls.py


from base_project.settings import CURRENT_SITE, BRAND, SLOGAN

class HomeView(View):

    def get(self, request, *args, **kwargs):

        title = 'SEO meta title'
        meta_description = 'Seo meta description'
        social_title = title
        image = '/media/main/brand.webp'

        context = {
            'site': CURRENT_SITE,
            'brand': BRAND,
            'slogan': SLOGAN,
            'title': title,
            'meta_description': meta_description,
            'social_title': social_title,
            'social_description': meta_description,
            'image': image,
        }

        return render(request, 'home.html', context)
    
class AboutUsView(View):

    def get(self, request):

        title = 'About Us'
        meta_description = 'About Us'
        social_title = title
        image = '/media/main/brand.webp'

        context = {
            'site': CURRENT_SITE,
            'brand': BRAND,
            'slogan': SLOGAN,
            'title': title,
            'meta_description': meta_description,
            'social_title': social_title,
            'social_description': meta_description,
            'image': image,
        }

        return render(request, 'about_us.html', context)
    
class CookiesView(View):

    def get(self, request):

        title = 'Cookie Policy'
        meta_description = 'Cookie Policy'
        social_title = title
        image = '/media/main/brand.webp'

        context = {
            'site': CURRENT_SITE,
            'brand': BRAND,
            'slogan': SLOGAN,
            'title': title,
            'meta_description': meta_description,
            'social_title': social_title,
            'social_description': meta_description,
            'image': image,
        }

        return render(request, 'politics/cookies.html', context)
    
class LegalView(View):

    def get(self, request):

        title = 'Legal Notice'
        meta_description = 'Legal Notice'
        social_title = title
        image = '/media/main/brand.webp'

        context = {
            'site': CURRENT_SITE,
            'brand': BRAND,
            'slogan': SLOGAN,
            'title': title,
            'meta_description': meta_description,
            'social_title': social_title,
            'social_description': meta_description,
            'image': image,
        }

        return render(request, 'politics/legal.html', context)
    
class PrivacyView(View):

    def get(self, request):

        title = 'Privacy Policy'
        meta_description = 'Privacy Policy'
        social_title = title
        image = '/media/main/brand.webp'

        context = {
            'site': CURRENT_SITE,
            'brand': BRAND,
            'slogan': SLOGAN,
            'title': title,
            'meta_description': meta_description,
            'social_title': social_title,
            'social_description': meta_description,
            'image': image,
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