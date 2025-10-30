from django.shortcuts import render
from .serializers import *
from .models import *

from rest_framework.viewsets import ModelViewSet

# Create your views here.

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer