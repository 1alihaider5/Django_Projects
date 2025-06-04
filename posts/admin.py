from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at', 'image_preview']
    list_filter = ['user', 'created_at']
    search_fields = ['title', 'content', 'user__email']
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-height: 100px; max-width: 100px;" />'
        return "No Image"
    image_preview.allow_tags = True
    image_preview.short_description = 'Image Preview'