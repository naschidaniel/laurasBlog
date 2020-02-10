from rest_framework import serializers
from blog.models import BlogPost, BlogCategory
from pages.models import Pages

## Blog
class BlogPostSerializer(serializers.ModelSerializer):
    datePosted = serializers.DateTimeField(format='%Y-%m-%d %H:%M', input_formats=None)
    mainImage_url = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        many = True
        fields = ['id', 'title', 'subtitle', 'slug', 'datePosted', 'category', 'abstract', 'content', 'author', 'mainImage_url']

    def get_mainImage_url(self, blogPost):
        request = self.context.get('request')
        mainImage_url = blogPost.mainImage.url
        return request.build_absolute_uri(mainImage_url)
    
class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['id', 'category', 'slug', 'parent']

## Pages
class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pages
        fields = ['link', 'title', 'content', 'datePosted']