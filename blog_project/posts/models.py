from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    email =models.EmailField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Post(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey("Author", on_delete=models.CASCADE, related_name='posts')
    
    def __str__(self):
        return self.title




class Comment(models.Model):
    content = models.TextField(max_length=255)
    posted_by = models.CharField(max_length=100)
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.content