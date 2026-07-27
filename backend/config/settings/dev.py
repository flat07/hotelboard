# backend/config/settings/dev.py
from .base import *
from .env import env, env_list

DEBUG = env("DJANGO_DEBUG") == "True"
ALLOWED_HOSTS = env_list("DJANGO_ALLOWED_HOSTS")

CELERY_TASK_ALWAYS_EAGER = False
