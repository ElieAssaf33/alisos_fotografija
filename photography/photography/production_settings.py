from .settings import *
import os

DEBUG = False

# Update allowed hosts
ALLOWED_HOSTS = ['alisos-fotografija.onrender.com']  # Replace with your Render domain

# Configure static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Configure media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Update CSRF settings for Render
CSRF_TRUSTED_ORIGINS = ['https://alisos-fotografija.onrender.com']  # Replace with your Render domain

# Configure whitenoise for static files
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Add media file serving in production
MIDDLEWARE.append('django.middleware.security.SecurityMiddleware')
MIDDLEWARE.append('django.contrib.staticfiles.middleware.StaticFilesMiddleware') 