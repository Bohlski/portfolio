from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Category

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'blog/index.html'
	model = Post
	context_object_name = 'posts'
	queryset = Post.objects.order_by('-create_date') # Make newest blogposts come first


class PostView(generic.DetailView):
	template_name = 'blog/detail.html'
	model = Post
	context_object_name = 'post'


class CategoryView(generic.ListView):
	template_name = 'blog/category.html'
	model = Post
	context_object_name = 'posts'

	# Filter the posts by the category passed through the url
	def get_queryset(self):
		self.category = get_object_or_404(Category, name=self.kwargs['category'])
		return Post.objects.filter(categories__name__contains=self.category).order_by('-create_date')
	
	# Add the category url argument to the context object
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		# Add in the category
		context['category'] = self.kwargs['category']
		return context