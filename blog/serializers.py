from rest_framework import serializers
from .models import Post, Season, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model: Comment
        fields: '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'
