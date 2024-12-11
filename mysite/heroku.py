import os
import dj_database_url
from .settings import *

# Database Configuration
DATABASES = {
    "default": dj_database_url.config(
        default="sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3")
    )
}

# Debug Mode
DEBUG = False
TEMPLATE_DEBUG = False

# Static Files
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")  # Directory for collected static files
STATICFILES_DIRS = [os.path.join(BASE_DIR, "blogging/static")]  # Additional static files

# Whitenoise Configuration for Serving Static Files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Secret Key and Allowed Hosts
SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = ["*"]

# Middleware
MIDDLEWARE = (
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Must come before other middleware
    *MIDDLEWARE,
)
