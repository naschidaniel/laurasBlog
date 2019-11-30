from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from blog.models import BlogPosts
from pages.models import Pages

from api.serializers import BlogPostsSerializer, PagesSerializer


class BlogPostsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = BlogPosts.objects.all()
    serializer_class = BlogPostsSerializer

class PagesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Pages.objects.all()
    serializer_class = PagesSerializer
