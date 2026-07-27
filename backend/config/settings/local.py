# backend/config/settings/local.py

from .base import *
from .env import env, env_list

DEBUG = env("DJANGO_DEBUG") == "True"
ALLOWED_HOSTS = env_list("DJANGO_ALLOWED_HOSTS")
# CSRF_COOKIE_DOMAIN = ".lvh.me"
# SESSION_COOKIE_DOMAIN = ".lvh.me"
# CSRF_TRUSTED_ORIGINS = [
#     "http://serenity-spa.lvh.me:8000",
#     "http://*.lvh.me:8000",
# ]

INSTALLED_APPS += [
    # ...
    # "debug_toolbar",
    # "django_extensions",
    # ...
]
MIDDLEWARE += [
    # ...
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
    # ...
]
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
SECURE_CROSS_ORIGIN_OPENER_POLICY = None
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
