from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):

    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all().order_by('-posted_at')
    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_fields = [
        'author'
    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
