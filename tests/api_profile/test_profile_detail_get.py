import json
from faker import Faker
from django.contrib.auth.models import User
import pytest
from api_profile.serializers import UserSerializer


fake = Faker()

@pytest.mark.django_db
def test_get_invalid_id(admin_client):
    """Test get with invalid id
        Expect:
            - status code: 400
    """
    path = f'/profiles/{100}'
    response = admin_client.get(path)
    
    assert response.status_code == 404
    

@pytest.mark.django_db
def test_get_profile(admin_client):
    """Test get profile by id
        Expect:
            - status code: 200
            - data: User instance
    """
    user = User.objects.create_user(
        username=fake.name().split()[-1], password=fake.password()
    )
    user.save()
    
    path = f'/profiles/{user.id}'
    response = admin_client.get(path)
    
    assert response.status_code == 200
    assert response.data == UserSerializer(user).data
    
@pytest.mark.django_db
def test_get_403(client):
    """Test get with invalid id
        Expect:
            - status code: 400
    """
    path = f'/profiles/{100}'
    response = client.get(path)
    
    assert response.status_code == 403
    
def test_get_client_not_admin(client, django_user_model):
    """Erro 403 because is not your profile"""
    username = "user1"
    password = "bar"
    # user to login
    django_user_model.objects.create_user(username=username, password=password)
    # diferent user
    user = django_user_model.objects.create_user(username="user2", password=password)
    # Use this:
    client.force_login(user)
    # Or this:
    client.login(username=username, password=password)
    path = f'/profiles/{user.id}'
    response = client.get(path)
    assert response.status_code == 403

def test_get_your_own_profile(client, django_user_model):
    """Test if user can get your own profile"""
    username = "user1"
    password = "bar"
    user = django_user_model.objects.create_user(username=username, password=password)
    # Use this:
    client.force_login(user)
    # Or this:
    client.login(username=username, password=password)
    path = f'/profiles/{user.id}'
    response = client.get(path)
    assert response.status_code == 200

def test_get_your_own_admin_client(client, django_user_model):
    """Test if user can get your own profile"""
    username = "user1"
    password = "bar"
    user = django_user_model.objects.create_user(username=username, password=password)
    # Use this:
    client.force_login(user)
    path = f'/profiles/{user.id}'
    response = client.get(path)
    assert response.status_code == 200