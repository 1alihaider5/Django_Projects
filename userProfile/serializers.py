from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(required=False, allow_null=True)
    
    class Meta:
        model = Profile
        fields = ['id', 'name', 'bio', 'picture']
        read_only_fields = ['id']
        
    def to_representation(self, instance):
        """Custom representation to include full URL for picture"""
        representation = super().to_representation(instance)
        if instance.picture:
            representation['picture'] = instance.picture.url
        else:
            representation['picture'] = None
        return representation