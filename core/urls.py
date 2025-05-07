from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap

from .views import TemplateView, HomeView, AboutUsView, CookiesView, LegalView, PrivacyView, SitemapView

sitemaps = {
    'static': SitemapView,
}

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.users.urls')),  # Include user-related URLs
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('cookies/', CookiesView.as_view(), name='cookies'),
    path('legal/', LegalView.as_view(), name='legal'),
    path('privacy/', PrivacyView.as_view(), name='privacy'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'), # Sitemap
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type="text/plain"), name='robots'), # robots.txt
]

# Static files route
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
