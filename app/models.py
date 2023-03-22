from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
	name = models.CharField('Названия поста', max_length=256, blank=True, null=True)
	hashtag = models.CharField('Хештег', max_length=500, blank=True, null=True)
	img = models.ImageField('Изображения Поста')
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name