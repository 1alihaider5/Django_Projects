from django.db import models
from django.conf import settings
import os

def profile_image_path(instance, filename):
    """Generate path for profile pictures"""
    ext = filename.split('.')[-1]
    filename = f"profile_{instance.user.id}.{ext}"
    return os.path.join('profile_pics', filename)

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='profile'
    )
    name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    picture = models.ImageField(
        upload_to=profile_image_path, 
        null=True, 
        blank=True,
        default='profile_pics/default.png'
    )
    
    def __str__(self):
        return f"{self.user.email}'s Profile"