from django.shortcuts import render
from django.views import generic
from .models import Project

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'projects/index.html'
	model = Project
	context_object_name = 'projects'


class DetailView(generic.DetailView):
	# The whole slug is simply provided to the view, but if the slug is to be truncated in any sense, 
	# this needs to be expressed here
	template_name = 'projects/detail.html'
	model = Project