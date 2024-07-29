from .base import *
import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}