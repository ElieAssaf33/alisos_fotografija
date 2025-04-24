from django.contrib import admin
from .models import PhotoGallery, Photo, Review
from django.utils.html import format_html

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 3
    fields = ('image', 'title', 'description', 'order')
    ordering = ['order']

@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'photo_count')
    list_filter = ('category', 'created_at')
    search_fields = ('title',)
    inlines = [PhotoInline]
    
    def photo_count(self, obj):
        return obj.photos.count()
    photo_count.short_description = 'Photos'

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'gallery', 'image_preview')
    list_filter = ('gallery__category',)
    search_fields = ('title', 'description')
    ordering = ['gallery', 'order']
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.image.url)
        return "No image"
    image_preview.short_description = 'Preview'

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'rating', 'created_at', 'photo_preview')
    list_filter = ('rating', 'created_at')
    search_fields = ('client_name', 'review_text')
    ordering = ['-created_at']
    
    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.photo.url)
        return "No photo"
    photo_preview.short_description = 'Photo'