from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Post, Comment

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    author = post.author  # Get the author related to this post
    comments = post.comments.all()
    return render(request, 'posts/post_detail.html', {'post': post, 'comments': comments, 'author': author})

def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    return render(request, 'posts/author_detail.html', {'author': author})
