from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView

from api_profile.serializers import UserSerializer



class ProfilesView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self,request, pk, format=None):
        try:    
            profile = User.objects.get(pk=pk)
            serializer = UserSerializer(profile)
        except User.DoesNotExist as e:
            return Response(status=201)
        else:
            return Response(serializer.data)

class ProfilesViewList(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        profiles = User.objects.all()
        serializer = UserSerializer(profiles, many=True)
        return Response(serializer.data)
