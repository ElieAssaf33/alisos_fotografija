from django.apps import AppConfig


class PhotoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'photo'

    
    class Meta:
        verbose_name = 'photos '
        
    def ready(self):
                import photo.signals

      # This ensures signals are loaded