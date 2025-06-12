from rest_framework import serializers
from .models import Post, AutomationForm
from comments.serializers import CommentSerializer, LikeSerializer
from users.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "id",
            "user",
            "title",
            "content",
            "image",
            "image_url",
            "created_at",
            "updated_at",
            "likes",
            "comments",
        ]
        read_only_fields = ["id", "user", "created_at", "updated_at"]

    def get_likes(self, obj):
        return LikeSerializer(obj.likes.filter(liked=True), many=True).data

    def get_image_url(self, obj):
        """Use the model's safe image_url property"""
        return obj.image_url


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "content", "image"]
        extra_kwargs = {"image": {"required": False, "allow_null": True}}

    def to_internal_value(self, data):
        """Handle both form-data and JSON"""
        if hasattr(data, "getlist"):  # form-data
            return {
                "title": data.get("title"),
                "content": data.get("content"),
                "image": data.get("image"),
            }
        return super().to_internal_value(data)


# === AutomationProcess serializer ===


class AutomationFormSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user_details = UserSerializer(source="user", read_only=True)

    class Meta:
        model = AutomationForm
        fields = [
            "user",
            "user_details",
            "id",
            "title",
            "description",
            "frequency",
            "friction",
            "density",
        ]
