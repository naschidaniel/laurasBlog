from rest_framework import serializers
from blog.models import Post
from pages.models import Page

## Blog
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'datePosted', 'author']


## Pages
class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['title', 'content', 'datePosted']