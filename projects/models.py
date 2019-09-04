import os
from django.db import models
from django.utils.text import slugify
from portfolio.settings import BASE_DIR

# Create your models here.
class Project(models.Model):
	title = models.CharField(max_length=100)
	desc = models.TextField()
	tech = models.CharField(max_length=40)
	image = models.FilePathField(path=os.path.join(BASE_DIR, 'projects\\static\\img'))
	slug = models.SlugField(default='', unique=True)

	def __str__(self):
		return self.title

	# Override save to ensure a slug is created of the title
	# TODO: Need to actually ensure uniqueness and make requirements on length (use uuid for padding, is an idea)
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super().save(*args, **kwargs)