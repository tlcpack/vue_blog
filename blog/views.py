from django.shortcuts import render
from .models import Post, Season
from .serializers import PostSerializer, SeasonSerializer
from rest_framework import generics

# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class SeasonList(generics.ListCreateAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

class SeasonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer