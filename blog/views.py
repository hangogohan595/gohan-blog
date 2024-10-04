from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

# Create your views here.
all_posts = [
    {
        'slug': 'the-power-of-react',
        'image': 'https://picsum.photos/400',
        'author': 'Gohan',
        'date': date(2024, 10, 3),
        'title': 'The Power of React',
        'description': 'There\'s nothing like the frontend framework React',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Adipisci magni voluptas, nulla eius dolores dignissimos accusamus nam repudiandae velit vel, facere at dolore placeat. Sunt possimus voluptatum impedit quas temporibus.'
    },
    {
        'slug': 'the-power-of-django',
        'image': 'https://picsum.photos/400',
        'author': 'Gohan',
        'date': date(2024, 10, 4),
        'title': 'The Power of Django',
        'description': 'There\'s nothing like the framework Django',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Adipisci magni voluptas, nulla eius dolores dignissimos accusamus nam repudiandae velit vel, facere at dolore placeat. Sunt possimus voluptatum impedit quas temporibus.'
    },
    {
        'slug': 'the-power-of-laravel',
        'image': 'https://picsum.photos/400',
        'author': 'Gohan',
        'date': date(2024, 10, 4),
        'title': 'The Power of PHP Laravel',
        'description': 'There\'s nothing like the Laravel',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Adipisci magni voluptas, nulla eius dolores dignissimos accusamus nam repudiandae velit vel, facere at dolore placeat. Sunt possimus voluptatum impedit quas temporibus.'
    }
]

sorted_posts = sorted(all_posts, key=lambda post: post['date'])
latest_posts = sorted_posts[-3:]


def home(request):
    return render(request, 'blog/home.html', {'posts': latest_posts})


def posts(request):
    return render(request, 'blog/posts.html', {'posts': latest_posts})


def post(request, slug):
    post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post.html', {'post': post})
