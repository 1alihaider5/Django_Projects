

from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'content', 'image', 'image_url', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

    def get_image_url(self, obj):
        """Use the model's safe image_url property"""
        return obj.image_url

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        extra_kwargs = {
            'image': {'required': False, 'allow_null': True}
        }

    def to_internal_value(self, data):
        """Handle both form-data and JSON"""
        if hasattr(data, 'getlist'):  # form-data
            return {
                'title': data.get('title'),
                'content': data.get('content'),
                'image': data.get('image')
            }
        return super().to_internal_value(data)