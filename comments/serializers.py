from rest_framework import serializers
from .models import  Comment ,Like
from users.serializers import UserSerializer 
# from users.serializers import UserSerializer


class CommentSerializer (serializers.ModelSerializer):

    user = UserSerializer(read_only=True )
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
       model = Comment
       fields = ['user','content', 'created_at']  
       
       
class LikeSerializer (serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user = UserSerializer(read_only=True )
    class Meta:
        model = Like
        fields = ['user','liked','created_at' ] 