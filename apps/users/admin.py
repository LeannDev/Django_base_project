from django.contrib import admin
from django.conf import settings

from .models import User

admin.site.site_header = f"Admin panel - {settings.BRAND}"
admin.site.site_title = f"{settings.BRAND}"
admin.site.index_title = "Admin"

admin.site.register(User)