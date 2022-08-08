from django.db import models

from notifications.models import Notification
from post.models import Post
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def user_commented_post(sender, instance, *args, **kwargs):
        comment = instance
        post = comment.post
        sender = comment.user
        text_preview = comment.content[:90]
        notify = Notification(post=post, sender=sender, user=post.user, text_preview=text_preview, notification_type=2)
        notify.save()




post_save.connect(Comment.user_commented_post, sender=Comment)
