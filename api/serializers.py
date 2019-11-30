from rest_framework import serializers
from blog.models import BlogPosts
from pages.models import Pages

## BlogPosts
class BlogPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPosts
        fields = ['title', 'content', 'datePosted', 'author']


## Pages
class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pages
        fields = ['title', 'content', 'datePosted']