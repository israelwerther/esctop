import os
from decouple import config, Csv
from dj_database_url import parse as dburl
from google.oauth2 import service_account
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from pathlib import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=Csv())

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Apps de terceiros
    'widget_tweaks',
    # 'bootstrapform',
    # 'datetimepicker',
    # 'bootstrap_modal_forms',
    'dbbackup',
    
    #Minhas apps
    'projeto.core',
    'projeto.produto',
    'projeto.emprestimo',    
    'projeto.estoque',
    'projeto.cliente',
    'projeto.cliente_cnpj',
    'projeto.avalista',
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'projeto.urls'

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

WSGI_APPLICATION = 'projeto.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = {
	'default': config('DATABASE_URL', default=default_dburl, cast=dburl), 
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = False

#NÃO APAGAR ESSES MODELOS ABAIXO DE INPUTS
# DATE_INPUT_FORMATS = [
#     '%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', # '2006-10-25', '10/25/2006', '10/25/06'
#     '%b %d %Y', '%b %d, %Y',            # 'Oct 25 2006', 'Oct 25, 2006'
#     '%d %b %Y', '%d %b, %Y',            # '25 Oct 2006', '25 Oct, 2006'
#     '%B %d %Y', '%B %d, %Y',            # 'October 25 2006', 'October 25, 2006'
#     '%d %B %Y', '%d %B, %Y',            # '25 October 2006', '25 October, 2006'
# ]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'core:index'
LOGOUT_REDIRECT_URL = 'login'



if not DEBUG:
    GS_DATA = {
        "type": "service_account",
        "project_id": config("GS_PROJECT_ID", default="GS_PROJECT_ID"),
        "private_key_id": config("GS_PRIVATE_KEY_ID", default="GS_PRIVATE_KEY_ID"),
        "client_email": config("GS_CLIENT_EMAIL", default="GS_CLIENT_EMAIL"),
        "private_key": config("GS_PRIVATE_KEY", default="GS_PRIVATE_KEY").replace("\\n", "\n"),
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/esctopservice%40esctop.iam.gserviceaccount.com"
    }
    GS_CREDENTIALS = service_account.Credentials.from_service_account_info(GS_DATA)
    DBBACKUP_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    DBBACKUP_STORAGE_OPTIONS = {
        "bucket_name": config('GS_BACKUPS_BUCKET_NAME', default='GS_BACKUPS_BUCKET_NAME'),
        "project_id": config("GS_PROJECT_ID", default="GS_PROJECT_ID"),
        "blob_chunk_size": 1024 * 1024,
        "location": 'esctopdb/'
    }
    
    sentry_sdk.init(
        dsn=config('SENTRY_DSN', default='default'),
        integrations=[
            DjangoIntegration(),
        ],

        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=0.1,

        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True
    )

