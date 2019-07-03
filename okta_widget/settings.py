"""
Django settings for okta_widget project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'not_a_secret_for_dev#!@12345'
if os.environ.get('SECRET_KEY') is not None:
    SECRET_KEY = os.environ['SECRET_KEY']

if os.environ.get('SECRET_KEY') is not None:
    SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = True
if os.environ.get('DEBUG') is not None:
    DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = ['172.17.0.2','localhost', '127.0.0.1', '[::1]']
if os.environ.get('ALLOWED_HOSTS') is not None:
    ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(',')

# UNIDEMO_API = os.environ.get('UNIDEMO_API')
UDP_BASE_URL = os.environ.get('UDP_BASE_URL')
UDP_KEY = os.environ.get('UDP_KEY')
URL = os.environ.get('URL')
DEFAULT_PORT = os.environ.get('DEFAULT_PORT')
OKTA_ORG = os.environ.get('OKTA_ORG')
AUTH_SERVER_ID = os.environ.get('AUTH_SERVER_ID')
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
GOOGLE_IDP = os.environ.get('GOOGLE_IDP_ID')
FB_IDP = os.environ.get('FB_IDP_ID')
LNKD_IDP = os.environ.get('LNKD_IDP_ID')
SAML_IDP = os.environ.get('SAML_IDP_ID')
API_KEY = os.environ.get('API_KEY')
CUSTOM_LOGIN_URL = os.environ.get('CUSTOM_LOGIN_URL')
DEFAULT_SCOPES = os.environ.get('DEFAULT_SCOPES')
BASE_TITLE = os.environ.get('HTML_TITLE')
BASE_ICON = os.environ.get('ORGANIZATION_LOGO')
BACKGROUND_IMAGE_DEFAULT = os.environ.get('BACKGROUND_IMAGE')
BACKGROUND_IMAGE_CSS = os.environ.get('BACKGROUND_IMAGE_CSS')
BACKGROUND_IMAGE_AUTHJS = os.environ.get('BACKGROUND_IMAGE_AUTHJS')
BACKGROUND_IMAGE_IDP = os.environ.get('BACKGROUND_IMAGE_IDP')
REDIRECT_URI = os.environ.get('REDIRECT_URI')
IDP_DISCO_PAGE = os.environ.get('IDP_DISCO_PAGE')
LOGIN_NOPROMPT_BOOKMARK = os.environ.get('LOGIN_NOPROMPT_BOOKMARK')

APP_PERMISSIONS_CLAIM = os.environ.get('APP_PERMISSIONS_CLAIM')
API_PERMISSIONS_CLAIM = os.environ.get('API_PERMISSIONS_CLAIM')

DELEGATION_SERVICE_ENDPOINT = os.environ.get('DELEGATION_SERVICE_ENDPOINT')

# IMPERSONATION_VERSION = os.environ.get('IMPERSONATION_VERSION')
# IMPERSONATION_ORG = os.environ.get('IMPERSONATION_ORG')
# IMPERSONATION_ORG_AUTH_SERVER_ID = os.environ.get('IMPERSONATION_ORG_AUTH_SERVER_ID')
# IMPERSONATION_ORG_OIDC_CLIENT_ID = os.environ.get('IMPERSONATION_ORG_OIDC_CLIENT_ID')
# IMPERSONATION_ORG_REDIRECT_IDP_ID = os.environ.get('IMPERSONATION_ORG_REDIRECT_IDP_ID')
# IMPERSONATION_SAML_APP_ID = os.environ.get('IMPERSONATION_SAML_APP_ID')
#
# IMPERSONATION_V2_ORG = os.environ.get('IMPERSONATION_V2_ORG')
# IMPERSONATION_V2_SAML_APP_ID = os.environ.get('IMPERSONATION_V2_SAML_APP_ID')
# IMPERSONATION_V2_ORG_API_KEY = os.environ.get('IMPERSONATION_V2_ORG_API_KEY')
# IMPERSONATION_V2_SAML_APP_EMBED_LINK = os.environ.get('IMPERSONATION_V2_SAML_APP_EMBED_LINK')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    'bootstrap3',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'okta_widget.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['Templates'],
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

WSGI_APPLICATION = 'okta_widget.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATIC_URL = '/static/'
STATIC_ROOT = "/var/www/unidemo/static/"

CORS_URLS_REGEX = r'^/oauth/.*$'

CORS_ORIGIN_ALLOW_ALL = False


