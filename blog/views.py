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


class CategoryView(generic.ListView):
	template_name = 'blog/category.html'
	model = Post
	context_object_name = 'posts'

	def get_queryset(self):
		print('TESTING')
		self.category = get_object_or_404(Category, name=self.kwargs['category'])
		print(self.category)
		return Post.objects.filter(categories__name__contains=self.category).order_by('-create_date')
	
	# Need to add the categories to the context object
	#def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
	#	context = super().get_context_data(**kwargs)
		# Add in a QuerySet of all the categories
	#	context['categories'] = Category.objects.all()
	#	return context