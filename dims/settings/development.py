from .base import *
import cloudinary

import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.getenv("Pro_CLOUD_NAME"),
    "API_KEY": os.getenv("Pro_API_KEY"),
    "API_SECRET": os.getenv("Pro_API_SECRET"),
    "FOLDER": "dims_media",
}

DEFAULT_FILE_STORAGE = os.getenv("DEFAULT_FILE_STORAGE")

# email set up
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_PASSWORD")