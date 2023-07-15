from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework.views import APIView

from api_profile.serializers import UserSerializer


class ListProfiles(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, format=None):
        profiles = User.objects.all()
        serializer = UserSerializer(profiles, many=True)
        return Response(serializer.data)
