from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model
import re
import os

User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()  

    class Meta:
        model = Post
        fields = ['id','title', 'image', 'content', 'author']

    # No need to override create() here

    def get_author(self, obj):
        return {
            "id": obj.author.id,
            "username": obj.author.username,
            "email": obj.author.email,
            "first_name": obj.author.first_name,
            "last_name": obj.author.last_name,
        }

    def update(self, instance, validated_data):
        new_image = validated_data.get('image', None)
        if new_image and instance.image:
            instance.image.delete(save=False)
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
    


class AuthorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password', 'first_name', 'last_name']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')  
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        user.set_password(validated_data['password'])  
        user.save()
        return user
    


   
