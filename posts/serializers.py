from rest_framework import serializers
from .models import Post
from useraccounts.serializers import ProfileSerializer


class PostSerializer(serializers.ModelSerializer):
    """Post Serializer"""
    owner = ProfileSerializer(many=False)
    likes = ProfileSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'


