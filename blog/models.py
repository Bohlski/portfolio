from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=20)
	
	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=255)
	body = models.TextField()
	create_date = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	categories = models.ManyToManyField('Category', related_name='posts')
	slug = models.SlugField(default='', unique=True)

	def __str__(self):
		return self.title

	# Override save to ensure a slug is created of the title
	# TODO: Need to actually ensure uniqueness and make requirements on length (use uuid for padding, is an idea)
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super().save(*args, **kwargs)

# Can perhaps add comments later if you find that amusing..