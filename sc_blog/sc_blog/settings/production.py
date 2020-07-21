import dj_database_url
from decouple import config

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
ADMINS = (('Neil', 'neil@neilmillard.com'),)

# Console will be picked up by gunicorn
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
    },
    # https://docs.djangoproject.com/en/3.0/topics/logging/#django-security
    'loggers': {
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
}

GOOGLE_CAPTCHA_SITE_KEY = '6Lf50ucUAAAAAF3dJuv37mVgmjVmqKe6pIxg4R0X'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
EMAIL_USE_TLS = False

STATIC_ROOT = config('STATIC_ROOT')
