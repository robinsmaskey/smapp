from rest_framework import serializers
from .models import Post, Comment
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


class PostCreateSerializer(serializers.ModelSerializer):
    """Post Create Serializer"""
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Post
        fields = ['title', 'content', 'owner', 'id']


class CommentCreateSerializer(serializers.ModelSerializer):
    """Comment Create Serializer"""
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Comment
        fields = ['content', 'post', 'owner', 'id']

