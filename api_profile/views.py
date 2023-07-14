from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api_profile.serializers import UserSerializer


@api_view(['GET'])
def list_profiles(request):
    profiles = User.objects.all()
    serializer = UserSerializer(profiles, many=True)
    return Response(serializer.data)
