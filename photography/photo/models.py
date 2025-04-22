from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from django.core.validators import MinValueValidator, MaxValueValidator

class PhotoGallery(models.Model):
    CATEGORY_CHOICES = [
        ('portrait', 'Portrait'),
        ('wedding', 'Wedding'),
        ('nature', 'Nature'),
        ('street', 'Street'),
        ('family', 'Family'),
        ('events', 'Events'),
        ('document', 'Documentary')
    ]
    
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='portrait')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.category} - {self.title}"

class Photo(models.Model):
    gallery = models.ForeignKey(PhotoGallery, on_delete=models.CASCADE, related_name='photos')
    image = ProcessedImageField(
        upload_to='images/',
        processors=[ResizeToFit(1920, 1080, upscale=False)],  # Resize to max 1920x1080
        format='JPEG',
        options={'quality': 90}  # Set JPEG quality to 90%
    )
    thumbnail = ProcessedImageField(
        upload_to='thumbnails/',
        processors=[ResizeToFit(400, 400, upscale=False)],
        format='JPEG',
        options={'quality': 85},  # Set JPEG quality to 85% for thumbnails
        null=True,  # Allow null values in database
        blank=True  # Allow empty values in forms
    )
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'id']
    
    def __str__(self):
        return f"{self.gallery.title} - {self.title if self.title else 'Untitled'}"

class Review(models.Model):
    client_name = models.CharField(max_length=100)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    review_text = models.TextField()
    photo = models.ImageField(upload_to='reviews/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f"Review by {self.client_name}"

    class Meta:
        ordering = ['-created_at']
