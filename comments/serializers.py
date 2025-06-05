from rest_framework import serializers
from .models import  Comment ,Like
# from users.serializers import UserSerializer


class CommentSerializer (serializers.ModelSerializer):

    # user = UserSerializer(read_only=True )
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
       model = Comment
       fields = ['user','user_id', 'content', 'post_id', 'created_at']  
       
       
class LikeSerializer (serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Like
        fields = ['user','user_id', 'post_id', 'liked','created_at' ] 