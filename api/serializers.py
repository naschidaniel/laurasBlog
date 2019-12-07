from rest_framework import serializers
from blog.models import BlogPost
from pages.models import Pages

## BlogPosts
class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'datePosted', 'author']


## Pages
class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pages
        fields = ['title', 'content', 'datePosted']