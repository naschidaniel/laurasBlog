from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from blog.models import Post
from api.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
