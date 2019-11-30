from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from blog.models import BlogPosts
from pages.models import Page

from api.serializers import BlogPostsSerializer, PageSerializer


class BlogPostsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = BlogPosts.objects.all()
    serializer_class = BlogPostsSerializer

class PageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Page.objects.all()
    serializer_class = PageSerializer
