from rest_framework import serializers
from blog.models import BlogPost, BlogCategory
from pages.models import Pages
from sociallinks.models import SocialMediaLink

class BlogPostSerializer(serializers.ModelSerializer):
    datePosted = serializers.DateTimeField(
        format='%Y-%m-%d %H:%M', input_formats=None)
    mainImage_url = serializers.SerializerMethodField()
    subImage1_url = serializers.SerializerMethodField()
    subImage2_url = serializers.SerializerMethodField()
    subImage3_url = serializers.SerializerMethodField()
    subImage4_url = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        many = True
        fields = ['id', 'title', 'subtitle', 'slug', 'datePosted', 'category', 'abstract', 'content', 'author',
                  'mainImage_url', 'mainImageAlt',
                  'subImage1_url', 'subImage1Alt',
                  'subImage2_url', 'subImage2Alt',
                  'subImage3_url', 'subImage3Alt',
                  'subImage4_url', 'subImage4Alt'
                  ]

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
        if blogPost.subImage2 != '':
            subImage2_url = blogPost.subImage2.url
            return_value = request.build_absolute_uri(subImage2_url)
        else:
            return_value = ''
        return return_value

    def get_subImage3_url(self, blogPost):
        request = self.context.get('request')
        if blogPost.subImage3 != '':
            subImage3_url = blogPost.subImage3.url
            return_value = request.build_absolute_uri(subImage3_url)
        else:
            return_value = ''
        return return_value

    def get_subImage4_url(self, blogPost):
        request = self.context.get('request')
        if blogPost.subImage4 != '':
            subImage4_url = blogPost.subImage4.url
            return_value = request.build_absolute_uri(subImage4_url)
        else:
            return_value = ''
        return return_value


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['id', 'category', 'slug', 'parent']

# Pages
class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pages
        fields = ['link', 'title', 'content', 'datePosted']

# SocialLinks
class SocialMediaLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaLink
        fields = ['socialMediaPlatform', 'url']