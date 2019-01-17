from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from blog.models import Post, Comment

# Create your views here.
def index(request):
	#return HttpResponse('This is my blog')
	return render(request, 'compurat/index.html')

def posts(request):
	all_posts = Post.objects.order_by('-created_on')
	context = {'posts_list' : all_posts}
	return render(request, 'blog/posts.html', context)
	#return HttpResponse('This is an individual post')

def post_detail(request, pid):
	post = get_object_or_404(Post, pk = pid)
	return render(request, 'blog/post_detail.html', {'post' : post})