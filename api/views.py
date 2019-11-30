from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from blog.models import Post
from pages.models import Page

from api.serializers import PostSerializer, PageSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Page.objects.all()
    serializer_class = PageSerializer
