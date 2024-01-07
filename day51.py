# Problem: Django - Static Files and Media
# Description: Manage static files and handle media in a Django project.
# Code (settings.py):

import os

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
