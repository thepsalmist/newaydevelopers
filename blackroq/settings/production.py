from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    "127.0.0.1",
    "109.74.193.206",
    "newwaydevelopers.co.ke",
    "www.blackroq.co.ke",
]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
