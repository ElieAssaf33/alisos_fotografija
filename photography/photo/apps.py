from django.apps import AppConfig


class PhotoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'photo'

    def ready(self):
        import photo.signals  # Ensures signals are loaded
    