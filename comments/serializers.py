from rest_framework import serializers
from .models import  Commnent
from users.serializers import UserSerializer


class CommentSerializer (serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
       model = Commnent
       fields = ['id', 'user', 'content', 'post', 'created_at']  
       read_only_fields = ['id', 'created_at' , 'user']    