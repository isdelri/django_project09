import os
import dj_database_url
from .settings import *

DATABASES = {
    "default": dj_database_url.config(
        default="sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3")
    )
}

DEBUG = False
TEMPLATE_DEBUG = False

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

SECRET_KEY = os.environ.get("SECRET_KEY", "fallback-secret-key")
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")

MIDDLEWARE = (
    "whitenoise.middleware.WhiteNoiseMiddleware",
    *MIDDLEWARE,
)
