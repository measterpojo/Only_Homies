import os


from django.db import models
from django.contrib.auth.models import User
# from post.models import Post

from django.db.models.signals import post_save

from posts.models import Bookmark
from PIL import Image

from django.conf import settings


def user_directory_path_pic(instance, filename):
	#file will be uploaded to Media_root/ user_<id>filename
	profile_pic_name = 'user_{0}/profile.jpg'.format(instance.user.id)
	full_path = os.path.join(settings.MEDIA_ROOT, profile_pic_name)


	if os.path.exists(full_path):
		os.remove(full_path)


	return profile_pic_name

def user_directory_path_banner(instance, filename):
	#file will be uploaded to Media_root/ user_<id>filename
	banner_pic_name = 'user_{0}/banner.jpg'.format(instance.user.id)
	full_path = os.path.join(settings.MEDIA_ROOT, banner_pic_name)


	if os.path.exists(full_path):
		os.remove(full_path)

	return banner_pic_name


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	# first_name = models.CharField(max_length=50)
	# last_name = models.CharField(max_length=50)
	location = models.CharField(max_length=50, null=True, blank=True)
	url = models.CharField(max_length=80, null=True, blank=True)
	profile_info = models.TextField(max_length=150, null=True, blank=True)
	created = models.DateField(auto_now_add=True)
	# favorites = models.ManyToManyField(Post)
	picture = models.ImageField(upload_to=user_directory_path_pic, blank=True, null=True)
	banner = models.ImageField(upload_to=user_directory_path_banner, blank=True, null=True)


	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		SIZE = 250,250

		if self.picture:
			pic = Image.open(self.picture.path)
			pic.thumbnail(SIZE, Image.LANCZOS)
			pic.save(self.picture.path)


		if self.banner:
			pic = Image.open(self.banner.path)
			pic.thumbnail(SIZE, Image.LANCZOS)
			pic.save(self.banner.path)

	def __str__ (self):
		return self.user.username

# signals
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
		Bookmark.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()



class PeopleList(models.Model):
	title = models.CharField(max_length=150)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='list_user')
	people = models.ManyToManyField(User, related_name='people_user') 

	def __str__(self):
		return self.title


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)













