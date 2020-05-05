from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post


# Create your views here.


def index(request):
	return render(request, 'blog/index.html', {})


def post_list(request):
	title = 'CleanBlog'
	subtitle = 'A Blog Theme by Start BootStrap'
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/post_list.html', {
		'title':title,
		'subtitle':subtitle,
		'posts':posts,
		})

def about(request):
	title = 'About Me'
	subtitle = 'This is what I do'
	return render(request, 'blog/about.html', {
		'title':title,
		'subtitle':subtitle,
		})

def contact(request):
	title = 'Contact Me'
	subtitle = 'This is it'
	return render(request, 'blog/contact.html', {
		'title':title,
		'subtitle':subtitle,
		})

def post_rev(request):
	title = Post.title
	subtitle = Post.description
	author = Post.author
	published_date = Post.published_date
	text = Post.text
	post = Post.objects.get(pk=pk)
	return render(request, 'blog/post_rev.html', {
		'title':title,
		'subtitle':subtitle,
		'author':author,
		'published_date':published_date,
		})

def post(request, pk):
	title = Post.title
	subtitle = Post.description
	author = Post.author
	published_date = Post.published_date
	text = Post.text
	# post = Post.objects.get(pk=pk)
	post = get_objects_or_404(Post, pk=pk)
	return render(request, 'blog/post.html', {
		'title':title,
		'subtitle':subtitle,
		'author':author,
		'published_date':published_date,
		'post': post,
		})

def post(request, pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request, 'blog/post.html', {'post': post,})