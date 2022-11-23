from rest_framework.decorators import api_view
from .serializers import UserRegisterSerializer, ProfileSerializer
from rest_framework import status
from rest_framework.response import Response
from .models import *
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer

@api_view(['POST'])
def register_user(request):
    """New User Register View"""
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def update_profile(request, profile_id):
    try:
        profile = Profile.objects.get(id=profile_id)
        serializer = ProfileSerializer(instance=profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


class MyTokenObtainPairView(TokenObtainPairView):
    """Token Obtain Pair View"""
    serializer_class = MyTokenObtainPairSerializer
