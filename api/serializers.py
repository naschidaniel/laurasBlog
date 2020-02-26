from rest_framework import serializers
from blog.models import BlogPost, BlogCategory
from pages.models import Pages

## Blog
class BlogPostSerializer(serializers.ModelSerializer):
    datePosted = serializers.DateTimeField(format='%Y-%m-%d %H:%M', input_formats=None)
    mainImage_url = serializers.SerializerMethodField()
    subImage1_url = serializers.SerializerMethodField()
    subImage2_url = serializers.SerializerMethodField()
    subImage3_url = serializers.SerializerMethodField()
    subImage4_url = serializers.SerializerMethodField()
    subImage5_url = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        many = True
        fields = ['id', 'title', 'subtitle', 'slug', 'datePosted', 'category', 'abstract', 'content', 'author', 'mainImage_url', 'subImage1_url', 'subImage2_url', 'subImage3_url', 'subImage4_url', 'subImage5_url']

    def get_mainImage_url(self, blogPost):
        request = self.context.get('request')
        mainImage_url = blogPost.mainImage.url
        return request.build_absolute_uri(mainImage_url)

    def get_subImage1_url(self, blogPost):
        request = self.context.get('request')
        if blogPost.subImage1 != '':
            subImage1_url = blogPost.subImage1.url
            return_value = request.build_absolute_uri(subImage1_url)
        else:
            return_value = ''
        return return_value

    def get_subImage2_url(self, blogPost):
        request = self.context.get('request')
        if blogPost.subImage1 != '':
            subImage1_url = blogPost.subImage1.url
            return_value = request.build_absolute_uri(subImage1_url)
        else:
            return_value = ''
        return return_value

    def get_subImage3_url(self, blogPost):
        request = self.context.get('request')
        if blogPost.subImage1 != '':
            subImage1_url = blogPost.subImage1.url
            return_value = request.build_absolute_uri(subImage1_url)
        else:
            return_value = ''
        return return_value

    def get_subImage4_url(self, blogPost):
        request = self.context.get('request')
        if blogPost.subImage1 != '':
            subImage1_url = blogPost.subImage1.url
            return_value = request.build_absolute_uri(subImage1_url)
        else:
            return_value = ''
        return return_value

    def get_subImage5_url(self, blogPost):
        request = self.context.get('request')
        if blogPost.subImage1 != '':
            subImage1_url = blogPost.subImage1.url
            return_value = request.build_absolute_uri(subImage1_url)
        else:
            return_value = ''
        return return_value

    
class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['id', 'category', 'slug', 'parent']

## Pages
class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pages
        fields = ['link', 'title', 'content', 'datePosted']