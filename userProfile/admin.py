from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'picture_preview']
    list_filter = ['user__is_active']
    search_fields = ['user__email', 'name']
    readonly_fields = ['picture_preview']
    
    def picture_preview(self, obj):
        if obj.picture:
            return f'<img src="{obj.picture.url}" style="max-height: 50px; max-width: 50px;" />'
        return "No Image"
    picture_preview.allow_tags = True
    picture_preview.short_description = 'Profile Picture'