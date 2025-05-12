import os
import base64
from pathlib import Path

from decouple import config, Csv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# Get the encryption key from environment variables
# SECURITY WARNING: keep the encryption key used in production secret!
ENCRYPTION_KEY = config("ENCRYPTION_KEY", default=None)

if ENCRYPTION_KEY is None:
    raise ValueError("ENCRYPTION_KEY must be set in the environment variables.")

# decode the encryption key
try:
    ENCRYPTION_KEY = base64.urlsafe_b64decode(ENCRYPTION_KEY)
    if len(ENCRYPTION_KEY) != 32:
        raise ValueError("ENCRYPTION_KEY must be 32 bytes long.")
except Exception as e:
    raise ValueError(f"Failed to decode ENCRYPTION_KEY: {e}")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='', cast=Csv())


# Application definition

BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_APPS = [
    'django.contrib.sitemaps',
]

LOCAL_APPS = [
    'apps.users.apps.UsersConfig',
    'apps.emails.apps.EmailsConfig',
    'apps.images.apps.ImagesConfig',
    'apps.profiles.apps.ProfilesConfig',
]

INSTALLED_APPS = BASE_APPS + THIRD_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATE_ROOT = os.path.join(BASE_DIR, 'core/templates')
USERS_TEMPLATE = os.path.join(BASE_DIR, 'apps/users/templates')
EMAILS_TEMPLATE = os.path.join(BASE_DIR, 'apps/emails/templates')
PROFILES_TEMPLATE = os.path.join(BASE_DIR, 'apps/profiles/templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_ROOT, USERS_TEMPLATE, EMAILS_TEMPLATE, PROFILES_TEMPLATE],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom user
AUTH_USER_MODEL = 'users.User'

# login and logout
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# enviroments
CURRENT_SITE = config('CURRENT_SITE', default='localhost')
BRAND = config('BRAND', default='my business')
SLOGAN = config('SLOGAN', default='my slogan')

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)  # TLS port
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)  # TLS
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST

# Password reset
PASSWORD_RESET_TIMEOUT = 60 * 60  # 1 hour

########################
### Loggings configs ###
########################

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'app.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': { # all django logs
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': True,
        },
        'core': {  # all logs from the core
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': False,
        },
    },
}