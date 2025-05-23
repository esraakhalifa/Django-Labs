from rest_framework import serializers
from .models import Post, Author
import re
import os

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
    # Show author details as read-only (optional: you can customize this as needed)
    author = serializers.StringRelatedField(read_only=True)  

    class Meta:
        model = Post
        fields = ['id','title', 'image', 'content', 'author']
        read_only_fields = ['author']  # Author is set by the server, not client

    # No need to override create() here

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    def to_representation(self, instance):
        data = super().to_representation(instance)
        image_field = instance.image
        if image_field and not os.path.isfile(image_field.path):
            # Set image to None if the file is missing
            data['image'] = None
        return data

   
