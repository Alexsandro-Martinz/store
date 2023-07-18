from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView

from api_profile.serializers import UserSerializer



@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def profiles_list(request):
    """
    List all profiles, or create a new profile
    """
    # List all profiles
    if request.method == 'GET':
        profiles = User.objects.all()
        serializer = UserSerializer(profiles, many=True)
        return Response(serializer.data)
    
    # Create a new profile
    if request.method == 'POST':
        serialized = UserSerializer(data=request.data)
        if serialized.is_valid():
            user = serialized.create(serialized.validated_data)
            data = UserSerializer(user).data
            return Response(status=200, data=data)
        
        else:
            return Response(status=404, data={'datail': 'Data not receved'})
        
        
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def profile_detail(request, pk):
    
    pass


