from .models import Post, Comment
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from useraccounts.serializers import ProfileSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_posts(request):

    """querying all posts"""
    posts = Post.objects.all().order_by('-created')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_my_posts(request, profile_id):
    """querying logged in user posts"""
    print(request.user)
    print(type(request.user))
    posts = Post.objects.filter(owner=profile_id)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)