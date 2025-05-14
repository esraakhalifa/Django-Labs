from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Post, Comment
from .serializers import PostSerializer, AuthorSerializer
from rest_framework import generics

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    author = post.author 
    comments = post.comments.all()
    return render(request, 'posts/post_detail.html', {'post': post, 'comments': comments, 'author': author})

def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    return render(request, 'posts/author_detail.html', {'author': author})

class AuthorsList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

