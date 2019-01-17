from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
	path('', views.index, name = 'index'),
	path('blog/posts', views.posts, name = 'posts'),
	path('blog/posts/<int:pid>/', views.post_detail, name = 'post_detail'),
	#path('$/', views.comments, name = 'comments'),
]