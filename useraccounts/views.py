from rest_framework.decorators import api_view
from .serializers import UserRegisterSerializer
from rest_framework import status
from rest_framework.response import Response


@api_view(['POST'])
def register_user(request):
    """New User Register View"""
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
