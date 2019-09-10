from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
	path('', views.IndexView.as_view(), name='blog_index'),
	path('<slug:slug>/', views.PostView.as_view(), name='blog_post'),
	path('category/<category>', views.CategoryView.as_view(), name='blog_category'),
]