from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'blog/home.html')


def posts(request):
    return render(request, 'blog/posts.html')


def post(request, slug):
    return render(request, 'blog/post.html')
