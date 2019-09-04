from django.db import models

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

	def __str__(self):
		return self.title

# Can perhaps add comments later if you find that amusing..