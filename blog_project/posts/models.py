from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Author(AbstractUser):
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='posts/',null=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey("Author", on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True) 
    def __str__(self):
        return self.title




class Comment(models.Model):
    content = models.TextField(max_length=255)
    posted_by = models.CharField(max_length=100)
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.content