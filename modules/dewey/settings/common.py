"""
Django settings for dewey project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

from django.core.exceptions import ImproperlyConfigured

SETTINGS_MODULE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULE_ROOT = os.path.dirname(SETTINGS_MODULE)
PROJECT_ROOT = os.path.dirname(MODULE_ROOT)

def get_env(variable):
    try:
        return os.environ[variable]
    except KeyError:
        message = 'Invalid settings. Please set the {} environment variable'.format(variable)
        raise ImproperlyConfigured(message)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['dewey.sfo.plos.org', 'dewey.soma.plos.org']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dewey',
    'djcelery',
    'environments',
    'hardware',
    'hosts',
    'networks',
    'rest_framework'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'dewey.urls'

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

WSGI_APPLICATION = 'dewey.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dewey',
        'USER' : 'dewey',
        'PASSWORD' : get_env('POSTGRES_PASSWORD'),
        'HOST' : 'localhost',
        'PORT' : ''
    },
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'


# Logging configuration

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
      'verbose': {
          'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
          'datefmt' : "%d/%b/%Y %H:%M:%S"
      },
      'simple': {
          'format': '%(levelname)s %(message)s'
      },
    },
    'handlers': {
      'file': {
          'level': 'DEBUG',
          'class': 'logging.handlers.RotatingFileHandler',
          'filename': os.path.join(PROJECT_ROOT, 'dewey.log'),
          'maxBytes' : 1024 * 1024 * 5,  # 5MiB
          'backupCount' : 5,
          'formatter': 'verbose'
      },
    },
    'loggers': {
      'django': {
          'handlers':['file'],
          'propagate': True,
          'level':'INFO',
      },
      'dewey' : {
          'handlers': ['file'],
          'level': 'DEBUG',
      },
    }
}


REST_FRAMEWORK = {
    'PAGE_SIZE': 25,
    'EXCEPTION_HANDLER': 'rest_framework_json_api.exceptions.exception_handler',
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework_json_api.pagination.PageNumberPagination',
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework_json_api.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework_json_api.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_METADATA_CLASS': 'rest_framework_json_api.metadata.JSONAPIMetadata',
}

JSON_API_FORMAT_KEYS = 'dasherize'
JSON_API_FORMAT_TYPES = 'dasherize'


# Jira integration for syncing assets

JIRA_USERNAME = get_env('JIRA_USERNAME')
JIRA_PASSWORD = get_env('JIRA_PASSWORD')
JIRA_URL = 'https://developer.plos.org/jira'


# Celery Task queue

BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend'
CELERYBEAT_SCHEDULER='djcelery.schedulers.DatabaseScheduler'

SITE_PROTOCOL = 'http'
SITE_DOMAIN = 'localhost:8000'

# Detect gunicorn
try:
  if 'gunicorn' in sys.argv[0]:
    FRONTEND = 'gunicorn'
  elif 'runserver' in sys.argv[1]:
    FRONTEND = 'runserver'
  else:
    FRONTEND = None
except IndexError:
  FRONTEND = None


NAGIOS_NETWORKS = ['soma-servers']

TASKS_ENABLED = True

APPEND_SLASH = True

PLOS_CA_CERTIFICATE = '/etc/ssl/certs/plos-ca.pem'
