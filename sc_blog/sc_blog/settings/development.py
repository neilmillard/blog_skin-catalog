from .base import *
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

GOOGLE_CAPTCHA_SITE_KEY = '6Lf--OcUAAAAANhGPZ0_Eu6zX0jJPzVWqTyKdmau'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
