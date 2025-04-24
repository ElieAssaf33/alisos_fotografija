from django.core.mail import send_mail
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Review
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpRequest

@receiver(post_save, sender=Review)
def send_review_email(sender, instance, created, **kwargs):
    """
    Send an email notification when a new review is created
    """
    if created:
        try:
            subject = f'New Review from {instance.client_name}'
            message = f"""
New Review Details:
Client Name: {instance.client_name}
Rating: {instance.rating}/5
Review Text: {instance.review_text}
Created At: {instance.created_at}

Please log into the admin panel to view full details.
            """
            send_mail(
                subject, 
                message, 
                settings.DEFAULT_FROM_EMAIL, 
                [settings.ADMIN_EMAIL],  # Replace with your email
                fail_silently=False,
            )
        except Exception as e:
            # Optional: You might want to log this error
            print(f"Failed to send review email: {e}")
        