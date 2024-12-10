import os
import dj_database_url
from mysite.settings import *  # Import base settings

# Configure database from DATABASE_URL environment variable or fallback to SQLite
DATABASES = {
    "default": dj_database_url.config(
        default="sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3")
    )
}

# Disable debug mode for production
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Define the static files root directory
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Configure secret key from environment variable
SECRET_KEY = os.environ.get("SECRET_KEY", "fallback-secret-key")

# Allow all hosts for now (make this more restrictive for production)
ALLOWED_HOSTS = ["*"]

# Add WhiteNoise to serve static files efficiently
MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
] + MIDDLEWARE  # Ensure WhiteNoise is added before other middleware

# Enable WhiteNoise for static file serving
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

