import os
from django.core.wsgi import get_wsgi_application

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fi.settings')

# Get the WSGI application
app = get_wsgi_application()  # Vercel expects `app`