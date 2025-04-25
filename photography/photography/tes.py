import os
import sys
from django.core.mail import send_mail
from django.conf import settings

# Add the project directory to PYTHONPATH
sys.path.append(r'c:\Users\eliju\OneDrive\Desktop\foto\alisos_fotografija\photography')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'photography.settings')

# Configure Django
import django
django.setup()

# Send test email
try:
    send_mail(
        'Test Email',
        'This is a test email from Django.',
        settings.EMAIL_HOST_USER,
        [settings.ADMIN_EMAIL],
        fail_silently=False,
    )
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")