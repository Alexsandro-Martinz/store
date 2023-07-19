import pytest
from django.contrib.auth.models import User
from faker import Faker

from api_profile.serializers import UserSerializer
from .datas import datas
import json

fake = Faker()
username: str = fake.name()
password: str = fake.password()

# Admin tests
def test_post_admin_200(admin_client):
    """Test post profile and save"""
    
    data = {
        "username": "Joseph+Smith",
        "password": "kV8qCdDl*t",
        "first_name": "Joseph",
        "last_name": "Smith",
        "email": "stacey82@example.net",
    }
    
    response = admin_client.post(
        '/profiles/', data
    )
    content = response.json()
    assert response.status_code == 200
    assert content['username'] == "Joseph+Smith"
    assert isinstance(content['id'], int)

def test_post_admin_400(admin_client):
    """
        Test create a new profile with invalid data
        Return: 400 status code
    """
    
    response = admin_client.post("/profiles/", {})
    assert response.status_code == 400

# User tests
@pytest.mark.django_db
def test_post_user_403(client):
    """
        Test post profile and save by user
        Return: 403 status code
    """

    User.objects.create_user(
        username=username,
        password=password
    ).save()
    
    data = {
        "username": "Joseph+Smith",
        "password": "kV8qCdDl*t",
        "first_name": "Joseph",
        "last_name": "Smith",
        "email": "stacey82@example.net",
    }
    client.login(username=username,password=password)
    response = client.post(
        '/profiles/', data
    )
    
    assert response.status_code == 403

# Client tests
def test_post_client_403(client):
    """
        Test post profile and save
        Return: 403 status code
    """
       
    data = {
        "username": "Joseph+Smith",
        "password": "kV8qCdDl*t",
        "first_name": "Joseph",
        "last_name": "Smith",
        "email": "stacey82@example.net",
    }
    
    response = client.post(
        '/profiles/', data
    )
    
    assert response.status_code == 403
