from .models import Post, Comment
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import PostSerializer, CommentSerializer, PostCreateSerializer, CommentCreateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from useraccounts.serializers import ProfileSerializer
from .permissions import IsOwnerOrReadOnly, has_permission_for_item
from rest_framework.exceptions import PermissionDenied


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
        # print(post)
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


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def update_post(request, post_id):
#     try:
#         post = Post.objects.get(id=post_id)
#         user = request.user
#         request_data = request.data
#         print(request_data)
#         updated_contents_list = request.data.keys()
#         if 'title' not in updated_contents_list: request_data['title'] = post.title
#         if 'content' not in updated_contents_list: request_data['content'] = post.content
#         request_data['owner'] = user.profile.id
#         print(request_data)
#         serializer = PostCreateSerializer(instance=post, data=request_data)
#         if serializer.is_valid():
#             serializer.save()
#             content = {'message': 'post updated'}
#         return Response(serializer.data, content)
#     except Post.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     finally:
#         content = {'message': 'failed to update the post'}
#         return Response(content, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_post(request, post_id):
    """delete post"""
    try:
        post = Post.objects.get(id=post_id)
        # print(post)
        if not has_permission_for_item(request, post):
            raise PermissionDenied()
        post.delete()
        content = {'message': 'post deleted'}
        return Response(content, status=status.HTTP_200_OK)
    except Post.DoesNotExist:
        content = {'message': 'Post Does Not Existed'}
        return Response(content, status=status.HTTP_404_NOT_FOUND)
    except PermissionDenied:
        return Response(PermissionDenied.default_detail, PermissionDenied.status_code)
    except:
        content = {'message': 'failed to delete the post'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_comment(request, post_id, comment_id):
    """delete comment"""
    try:
        comment = Comment.objects.get(id=comment_id)
        if not has_permission_for_item(request, comment):
            raise PermissionDenied()
        comment.delete()
        content = {'message': 'comment deleted'}
        return Response(content, status=status.HTTP_200_OK)
    except Comment.DoesNotExist:
        content = {'message': 'Comment Does Not Existed'}
        return Response(content, status=status.HTTP_404_NOT_FOUND)
    except PermissionDenied:
        content = {'message': PermissionDenied.default_detail}
        return Response(content, status=PermissionDenied.status_code)
    except:
        content = {'message': 'failed to delete the comment'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)


