from rest_framework import serializers
from .models import  Comment
from users.serializers import UserSerializer


class CommentSerializer (serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
       model = Comment
       fields = ['id','user', 'content', 'post', 'created_at']  
       