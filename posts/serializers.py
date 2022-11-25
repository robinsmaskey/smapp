from rest_framework import serializers
from .models import Post,Comment
from useraccounts.serializers import ProfileSerializer


class PostSerializer(serializers.ModelSerializer):
    """Post Serializer"""
    owner = ProfileSerializer(many=False)
    likes = ProfileSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Comment Serializer"""
    owner = ProfileSerializer(many=False)

    class Meta:
        model = Comment
        fields = '__all__'

