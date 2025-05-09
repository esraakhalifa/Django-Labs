from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = {
    1: {
        "title": "Welcome to Our Blog",
        "author": "Alice",
        "content": "We're excited to share our thoughts with you!",
        "date": "2025-05-01",
        "image_url": "images/post_1.jpeg"
    },
    2: {
        "title": "Learning Django Basics",
        "author": "Bob",
        "content": "Understanding models, views, and templates is essential.",
        "date": "2025-05-02",
        "image_url": "images/post_1.jpeg"
    },
    3: {
        "title": "Working with Django Admin",
        "author": "Charlie",
        "content": "The admin site is a powerful tool for managing data.",
        "date": "2025-05-03",
        "image_url": "images/post_1.jpeg"
    },
    4: {
        "title": "Tips for Clean Code",
        "author": "Dana",
        "content": "Write readable, maintainable, and well-documented code.",
        "date": "2025-05-04",
        "image_url": "images/post_1.jpeg"
    },
    5: {
        "title": "Python List Comprehensions",
        "author": "Eve",
        "content": "List comprehensions are a concise way to create lists.",
        "date": "2025-05-05",
        "image_url": "images/post_1.jpeg"
    },
    6: {
        "title": "Understanding Django ORM",
        "author": "Frank",
        "content": "Django ORM lets you query the database using Python.",
        "date": "2025-05-06",
        "image_url": "images/post_1.jpeg"
    },
    7: {
        "title": "Debugging in Django",
        "author": "Grace",
        "content": "Use the debug toolbar and logging to fix issues fast.",
        "date": "2025-05-07",
        "image_url": "images/post_1.jpeg"
    },
    8: {
        "title": "Using Django Forms",
        "author": "Hannah",
        "content": "Forms help validate and process user input securely.",
        "date": "2025-05-08",
        "image_url": "images/post_1.jpeg"
    },
    9: {
        "title": "Deploying Django Apps",
        "author": "Ian",
        "content": "Heroku, Vercel, or a VPS – many ways to go live.",
        "date": "2025-05-09",
        "image_url": "images/post_1.jpeg"
    },
    10: {
        "title": "What’s New in Django 5",
        "author": "Jane",
        "content": "Explore the newest features and improvements in Django.",
        "date": "2025-05-10",
        "image_url": "images/post_1.jpeg"
    }
}

def post_list(request):
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = posts.get(post_id)
    return render(request, 'posts/post_detail.html', {'post': post})