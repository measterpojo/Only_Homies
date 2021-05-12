from django.db import models

from posts.models import Post

from django.contrib.auth.models import User
from notification.models import Notification

from django.db.models.signals import post_save, post_delete

class Comments(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)


	def user_comment_post(sender, instance, *args, **kwargs):
		comment = instance
		post = comment.post
		sender = comment.user
		text_preview = comment.body[:50]

		notify = Notification(post=post, sender=sender, user=post.user, text_preview=text_preview ,notification_type=2)
		notify.save()

	def user_del_comment_post(sender, instance, *args, **kwargs):
		comment = instance
		post = comment.post
		sender = comment.user

		notify = Notification.objects.filter(post=post, sender=sender, user=post.user, notification_type=2)
		notify.delete()


post_save.connect(Comments.user_comment_post, sender=Comments)
post_delete.connect(Comments.user_del_comment_post, sender=Comments)