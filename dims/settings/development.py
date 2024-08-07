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
}

DEFAULT_FILE_STORAGE = os.getenv("DEFAULT_FILE_STORAGE")