from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from blog.models import BlogPost
from pages.models import Pages

from api.serializers import BlogPostSerializer, PagesSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class PagesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Pages.objects.all()
    serializer_class = PagesSerializer
