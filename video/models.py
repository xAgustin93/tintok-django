from distutils.command.upload import upload
import os
from django.db import models


def get_video_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.id, ext)
    return os.path.join('video/', filename)


def get_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.id, ext)
    return os.path.join('video_image/', filename)


class Video(models.Model):
    description = models.TextField()
    video = models.FileField(upload_to=get_video_path)
    image = models.ImageField(upload_to=get_image_path)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    share_counter = models.IntegerField(default=0)
    likes_counter = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class VideoLike(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    video = models.ForeignKey('video.Video', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
