from rest_framework import serializers
from blog.models import BlogPosts
from pages.models import Page

## BlogPosts
class BlogPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPosts
        fields = ['title', 'content', 'datePosted', 'author']


## Pages
class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['title', 'content', 'datePosted']