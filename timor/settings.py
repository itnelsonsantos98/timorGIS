"""
Django settings for timor project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

import django.conf.locale
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(g_ipc8-#q9-4a*vwbz)3!47j-8r4_y2tm4$2k8yyo5z$l$30c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'map',
    'djrichtextfield',
    'django_extensions',
    'widget_tweaks',
    'rosetta',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'timor.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'timor.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'timor_db',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = [
    ('tet', _('Tetum')),
    ('en', _('English')),
]

EXTRA_LANG_INFO = {
    'tet': {
        'bidi': False,  # right-to-left
        'code': 'tet',
        'name': 'Tetum',
        'name_local': 'Tetum',  # unicode codepoints here
    },
}

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Add custom languages not provided by Django
# LANG_INFO = dict(django.conf.locale.LANG_INFO.items() + EXTRA_LANG_INFO.items())
django.conf.locale.LANG_INFO.update(EXTRA_LANG_INFO)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "map/static"),
]

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# Django Rich Text Field
TINYMCE_CONFIG = {
    'js': ['//tinymce.cachefly.net/4.1/tinymce.min.js'],
    'init_template': 'djrichtextfield/init/tinymce.js',
    'settings': {
        'menubar': False,
        'plugins': 'link image table code',
        'toolbar': 'formatselect | bold italic | removeformat |'
                   ' link unlink image table | code',
        'block_formats': 'Paragraph=p;Header 1=h1;Header 2=h2;Header 3=h3',
        'width': 700
    },
    'profiles': {
        'mini': {
            'toolbar': 'bold italic | removeformat'
        }
    }
}

CKEDITOR_CONFIG = {
    'js': ['//cdn.ckeditor.com/4.4.4/standard/ckeditor.js'],
    'init_template': 'djrichtextfield/init/ckeditor.js',
    'settings': {
        'toolbar': [
            {'items': ['Format', '-', 'Bold', 'Italic', '-', 'RemoveFormat']},
            {'items': ['Link', 'Unlink', 'Image', 'Table', 'Video']},
            {'items': ['Source']}
        ],
        'format_tags': 'p;h1;h2;h3',
        'width': 700,
    },
    'profiles': {
        'mini': {
            'toolbar': [
                {'items': ['Bold', 'Italic', '-', 'RemoveFormat']},
            ]
        }
    },
}

DJRICHTEXTFIELD_CONFIG = CKEDITOR_CONFIG

try:
    from .local_settings import *  # noqa
except ImportError:
    pass
