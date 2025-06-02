from django.db import models
from django.conf import settings
import os

def post_image_path(instance, filename):
    """Generate path for post images"""
    ext = filename.split('.')[-1]
    filename = f"post_{instance.user.id}_{instance.id}.{ext}"
    return os.path.join('post_images', filename)

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(
        upload_to=post_image_path,
        null=True,
        blank=True,
        default=None
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.user.email}"

    @property
    def image_url(self):
        """Safe URL access that won't raise errors"""
        if self.image and hasattr(self.image, 'url'):
            try:
                return self.image.url
            except ValueError:  
                return None
        return None