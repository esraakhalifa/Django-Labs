from rest_framework import serializers
from .models import Post, Author
import re

class AuthorSerializer(serializers.ModelSerializer):
    
    def validate_first_name(self,value):
        if not value.isalpha():
            raise serializers.ValidationError('First name must contain only letters.')
        return value

    def validate_last_name(self,value):
        if not value.isalpha():
            raise serializers.ValidationError('Last name must contain only letters.')
        return value
    
    def validate_phone_number(self,value):
        if not re.match(pattern=r'^\+?\d{10,15}$',value=value):
            raise serializers.ValidationError('Phone number format must be valid.')
        return value
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'phone_number', 'email']



class PostSerializer(serializers.ModelSerializer):
    author=AuthorSerializer()
    class Meta:
        model = Post
        fields = ['title', 'image_url', 'content', 'author']
    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author, created = Author.objects.get_or_create(**author_data)
        post = Post.objects.create(author=author,**validated_data)
        return post
    def update(self, instance, validated_data):
        author_data = validated_data.pop('author', None)

        if author_data:
            author = instance.author
            for attr, value in author_data.items():
                setattr(author, attr, value)
            author.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance


   
