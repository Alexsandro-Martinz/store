import pytest
from django.contrib.auth.models import User
from faker import Faker

from api_profile.serializers import UserSerializer
from .datas import datas
import json

fake = Faker()

@pytest.mark.django_db
def test_get_admin_200(admin_client):
    """Test: only super user can take this list
    """
    # Insert: 5 users on Database
    for d in datas:
        User.objects.create(
            username=d["username"],
            first_name=d["first_name"],
            last_name=d["last_name"],
            email=d["email"],
            password=fake.password(),
        ).save()
    
    serialized = User.objects.all()
    profiles = UserSerializer(serialized, many=True).data

    response = admin_client.get("/profiles/")
    content = response.json()

    assert response.status_code == 200
    assert content == profiles

# User tests
@pytest.mark.django_db
def test_get_user_403(client):
    """Test: User logged can not access a list users."""
    
    username = fake.name()[0]
    password = fake.password()

    User.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)
    response = client.get('/profiles/')
    assert response.status_code == 403

# Client tests
def test_get_client_403(client):
    response = client.get("/profiles/")
    assert response.status_code == 403
