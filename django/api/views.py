from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from blog.models import BlogPost, BlogCategory, BlogQuote
from pages.models import Pages
from sociallinks.models import SocialMediaLink

from api.serializers import BlogCategorySerializer, BlogPostSerializer, BlogQuoteSerializer, PagesSerializer, SocialMediaLinkSerializer


class BlogCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = BlogPost.objects.all()
    param = 'fadsfdafad'
    serializer_class = BlogPostSerializer

class BlogQuoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = BlogQuote.objects.all()
    param = 'fadsfdafad'
    serializer_class = BlogQuoteSerializer

class PagesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Pages.objects.all()
    serializer_class = PagesSerializer

class SocialMediaLinkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SocialMediaLink.objects.all()
    serializer_class = SocialMediaLinkSerializer
