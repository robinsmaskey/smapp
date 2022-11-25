from .models import Post, Comment
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import PostSerializer, CommentSerializer, PostCreateSerializer, CommentCreateSerializer
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
    posts = Post.objects.filter(owner=profile_id)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_post_comments(request, post_id):
    """Get Post Comments"""
    try:
        post = Post.objects.get(id=post_id)
        comments = post.comments.all()
        serialized_comments = CommentSerializer(comments, many=True)
        return Response(serialized_comments.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    user = request.user
    request_data = request.data
    request_data['owner'] = user.profile.id
    serializer = PostCreateSerializer(data=request_data)

    if serializer.is_valid():
        serializer.save()
        content = {'post_id': serializer.data['id']}
        return Response(content, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request, post_id):
    user = request.user
    request_data = request.data
    request_data['owner'] = user.profile.id
    request_data['post'] = post_id
    serializer = CommentCreateSerializer(data=request_data)

    if serializer.is_valid():
        serializer.save()
        content = {'comment_id': serializer.data['id']}
        return Response(content, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_like_to_post(request, post_id):
    user = request.user
    profile = user.profile

    try:
        post = Post.objects.get(id=post_id)
        print(post)
        liked = False
        if post.likes.filter(id=profile.id).exists():
            post.likes.remove(profile)
            liked = False
            content = {'message': 'like reverted successfully', 'liked': liked}
        else:
            post.likes.add(profile)
            liked = True
            content = {'message': 'like added successfully', 'liked': liked}
        return Response(content, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
