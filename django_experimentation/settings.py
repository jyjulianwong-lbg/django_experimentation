"""
Django settings for django_experimentation project.

Generated by 'django-admin startproject' using Django 4.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path

from google.cloud import storage
from google.oauth2 import service_account

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-t%40f!k7^)yxw-q2ao4qxc-zlf6$z9_qh0=n6_(@#diov5z11d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "polls.apps.PollsConfig",
    "aarp_ingestion_module_test.apps.AarpIngestionModuleTestConfig",
    "google_cloud_bigquery.apps.GoogleCloudBigqueryConfig",
    "google_cloud_sql.apps.GoogleCloudSqlConfig",
    "google_cloud_storage.apps.GoogleCloudStorageConfig",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_experimentation.urls'

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

WSGI_APPLICATION = 'django_experimentation.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Copied from tnt01-audmsa-aarp-app/blob/main/AARP/settings.py. 

DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
DB_USER = os.getenv('DB_USER', '')
DB_PASS = os.getenv('DB_PASS', '')

database_defaults = {
    'HOST': DB_HOST,
    'USER': DB_USER,
    'PASSWORD': DB_PASS,
    'PORT': '6432',
    'OPTIONS': {
        'sslmode': 'disable'
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'application-db',
        **database_defaults,
    },
    'application-db': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'application-db',
        **database_defaults,
    },
    'automation-db': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'automation-db',
        **database_defaults,
    },
    'reporting-db': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'reporting-db',
        **database_defaults,
    },
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

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom: Google APIs and django-storages
STORAGES = None
GS_CREDENTIALS = None
GS_CLIENT = None
GS_PROJECT_ID = "tnt01-audmsa-bld-01-fdc2"
GS_BUCKET_NAME = "tnt01-audcda-bld-01-stb-euwe2-aarp"

_gs_creds_path = BASE_DIR / "google-app-creds" / "google-app-creds.json"
if os.path.exists(_gs_creds_path):
    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
        },
    }
    GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
        _gs_creds_path
    )
    GS_CLIENT = storage.Client.from_service_account_json(_gs_creds_path)
