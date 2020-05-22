from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post
from blog.forms import CommentForm

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.


def index(request):
	return render(request, 'blog/index.html', {})


def post_list(request):
	title = 'CleanBlog'
	subtitle = 'A Blog Theme by Start BootStrap'
	all_posts =  Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	posts = all_posts.filter(status=1) # published date
	paginator = Paginator(posts, 2)
	page_request_var = 'page'
	page = request.GET.get(page_request_var)

	try:
		post_list = paginator.page(page)
	except PageNotAnInteger:
		post_list = paginator.page(1)
	except EmptyPage:
		post_list = paginator.page(paginator.num_pages)



	return render(request, 'blog/post_list.html', {
		'title':title,
		'subtitle':subtitle,
		'page_request_var':page_request_var,
		'posts':post_list,
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
		'text':text,
		})


def post(request, pk):
	template_name = 'blog/post.html'
	post = get_object_or_404(Post, pk=pk)
	comments = post.comments.filter(active=True)
	new_comment = None

	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.post = post
			new_comment.save()

	else:
		comment_form = CommentForm()

	context = {
		'post':post,
		'comments':comments,
		'new_comment':new_comment,
		'comment_form':comment_form
	}


	return render(request, template_name, context)