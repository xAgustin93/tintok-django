from django.contrib import admin
from video.models import Video, VideoLike


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', "description", 'user', 'created_at')


@admin.register(VideoLike)
class VideoLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'video', 'created_at')
