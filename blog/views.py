from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
all_posts = Post.objects.all().order_by('-date')
latest_posts = all_posts[:3]


def home(request):
    return render(request, 'blog/home.html', {'posts': latest_posts})


def posts(request):
    return render(request, 'blog/posts.html', {'posts': latest_posts})


def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post.html', {'post': post, 'tags': post.tags.all()})
