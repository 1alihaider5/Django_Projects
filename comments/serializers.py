from rest_framework import serializers
from .models import  Comment ,Like
# from users.serializers import UserSerializer


class CommentSerializer (serializers.ModelSerializer):

    # user = UserSerializer(read_only=True )
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
       model = Comment
       fields = ['id','user','user_id', 'content', 'post', 'created_at']  
       
       
class LikeSerializer (serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Like
        fields = ['id', 'user','user_id', 'post', 'liked','created_at' ] 