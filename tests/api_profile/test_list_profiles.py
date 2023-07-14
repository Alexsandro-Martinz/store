import pytest
from django.contrib.auth.models import User

from api_profile.serializers import UserSerializer
from .datas import datas
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_get_list(client):
    for d in datas:
        User.objects.create(
            username=d["username"],
            email=d["email"],
            password=d["password"],
        ).save()
    profiles = User.objects.all()
    assert profiles.count() == 5
    
    profiles = User.objects.all()
    serializer = UserSerializer(profiles, many=True)

    response = client.get("/api-profile/")
    assert response.status_code == 200
    print(response.content)
    
    
