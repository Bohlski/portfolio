from django.urls import path
from . import views

app_name = 'projects'
urlpatterns = [
	path('', views.IndexView.as_view(), name='project_index'),
	path('<slug:slug>/', views.DetailView.as_view(), name='detail'),
]