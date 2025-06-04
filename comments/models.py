from django.db import models
# from django.conf import settings
from django.utils import timezone
from posts.models import Post
from users.models import User

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return  f"{self.content} by {self.user.email} on {self.post.title}"
    