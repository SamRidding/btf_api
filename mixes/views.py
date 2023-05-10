from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Mix
from .serializers import MixSerializer


class MixList(generics.ListCreateAPIView):

    serializer_class = MixSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Mix.objects.all().order_by('-posted_at')

    def perform_create(self, serializer):
        serializer.save()


class MixDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = MixSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Mix.objects.all().order_by('-posted_at')
