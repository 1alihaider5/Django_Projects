from django.db import models
from django.utils import timezone
from posts.models import Post
from users.models import User

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return  f"Comment {self.content} by {self.user.email} on Post {self.post.title}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post , on_delete=models.CASCADE, related_name='likes')
    liked = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
       
    def __str__(self):
        return f"Liked {self.liked} by {self.user.username} on post {self.post.title}"     