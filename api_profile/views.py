from rest_framework.decorators import APIView
from django.contrib.auth import login, logout, authenticate

from typing import Type
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404

from api_profile.serializers import UserSerializer

from rest_framework import generics
    

@api_view(["GET", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def profiles_list(request):
    """
    List all profiles, or create a new profile
    """
    # List all profiles
    if request.method == "GET":
        profiles = User.objects.all()
        serializer = UserSerializer(profiles, many=True)
        return Response(serializer.data)

    # Create a new profile
    elif request.method == "POST":
        serialized = UserSerializer(data=request.data)
        if serialized.is_valid():
            user = serialized.create(serialized.validated_data)
            data = UserSerializer(user).data
            return Response(status=status.HTTP_200_OK, data=data)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(["GET", "PUT", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def profile_detail(request, pk):
    
    if not (request.user.is_superuser or request.user.id == pk):
        return Response(status=status.HTTP_403_FORBIDDEN)
    
    try:
        user: Type[User] = get_object_or_404(User, pk=pk)
    except User.DoesNotExist:
        Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        return Response(status=status.HTTP_200_OK, data=UserSerializer(user).data)
    
    elif request.method == "PUT": 
        serialize = UserSerializer(data=request.data)
        if serialize.is_valid():
            user_updated = serialize.update(user, serialize.validated_data)
            data = UserSerializer(user_updated).data
            return Response(status=status.HTTP_200_OK, data=data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serialize.error_messages)

    elif request.method == "DELETE" and request.user.is_superuser:
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(['POST'])
def loginView(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = authenticate(username=username, password=password)
    
    if user is not None:
        login(request, user)
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def logoutView(request):
    user: User = request.user
    if not user.is_anonymous:
        logout(request)
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)