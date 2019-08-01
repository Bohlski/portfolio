from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'blog/index.html'
	model = Post
	context_object_name = 'posts'


class PostView(generic.DetailView):
	template_name = 'blog/detail.html'
	model = Post


class CategoryView(generic.ListView):
	template_name = 'blog/category.html'
	model = Post
	context_object_name = 'posts'