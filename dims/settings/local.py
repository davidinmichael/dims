from .base import *
import cloudinary
import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.getenv("CLOUD_NAME"),
    "API_KEY": os.getenv("API_KEY"),
    "API_SECRET": os.getenv("API_SECRET"),
    "FOLDER": "dims_media",
}

DEFAULT_FILE_STORAGE = os.getenv("DEFAULT_FILE_STORAGE")