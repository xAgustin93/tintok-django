from django.db import models


class Follow(models.Model):
    user = models.ForeignKey(
        'users.User', on_delete=models.CASCADE, related_name="user")
    user_followed = models.ForeignKey(
        'users.User', on_delete=models.CASCADE, related_name="user_followed")
    created_at = models.DateTimeField(auto_now_add=True)
