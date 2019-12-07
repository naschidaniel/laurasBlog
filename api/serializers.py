from rest_framework import serializers
from blog.models import BlogPost, BlogCategory
from pages.models import Pages

## Blog
class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'datePosted', 'author', 'category']

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['category', 'slug', 'parent']

## Pages
class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pages
        fields = ['title', 'content', 'datePosted']