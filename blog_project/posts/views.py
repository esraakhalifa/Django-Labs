from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = {
    1: {
        "title": "Welcome to Our Blog",
        "author": "Alice",
        "content": "We're excited to share our thoughts with you!",
        "date": "2025-05-01"
    },
    2: {
        "title": "Learning Django Basics",
        "author": "Bob",
        "content": "Understanding models, views, and templates is essential.",
        "date": "2025-05-02"
    },
    3: {
        "title": "Working with Django Admin",
        "author": "Charlie",
        "content": "The admin site is a powerful tool for managing data.",
        "date": "2025-05-03"
    },
    4: {
        "title": "Tips for Clean Code",
        "author": "Dana",
        "content": "Write readable, maintainable, and well-documented code.",
        "date": "2025-05-04"
    },
    5: {
        "title": "Python List Comprehensions",
        "author": "Eve",
        "content": "List comprehensions are a concise way to create lists.",
        "date": "2025-05-05"
    },
    6: {
        "title": "Understanding Django ORM",
        "author": "Frank",
        "content": "Django ORM lets you query the database using Python.",
        "date": "2025-05-06"
    },
    7: {
        "title": "Debugging in Django",
        "author": "Grace",
        "content": "Use the debug toolbar and logging to fix issues fast.",
        "date": "2025-05-07"
    },
    8: {
        "title": "Using Django Forms",
        "author": "Hannah",
        "content": "Forms help validate and process user input securely.",
        "date": "2025-05-08"
    },
    9: {
        "title": "Deploying Django Apps",
        "author": "Ian",
        "content": "Heroku, Vercel, or a VPS – many ways to go live.",
        "date": "2025-05-09"
    },
    10: {
        "title": "What’s New in Django 5",
        "author": "Jane",
        "content": "Explore the newest features and improvements in Django.",
        "date": "2025-05-10"
    }
}

def post_list(request):
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = posts.get(post_id)
    return render(request, 'posts/post_detail.html', {'post': post})