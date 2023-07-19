import json
from faker import Faker
from django.contrib.auth.models import User
import pytest
from api_profile.serializers import UserSerializer


fk = Faker()

data = {
    "username": "user2",
    "first_name": str(fk.name().split()[0]),
    "last_name": str(fk.name().split()[-1]),
    "email": str(fk.email()),
    "password": str(fk.password()),
}


# Admin tests
@pytest.mark.django_db
def test_put_admin_200(admin_client):
    user = User.objects.create_user(username="user1", password="pass1")
    user.save()
    path = f"/profiles/{user.id}"

    response = admin_client.put(path, data, content_type="application/json")
    content = response.json()
    assert content["username"] == data["username"]
    assert content["first_name"] == data["first_name"]
    assert content["last_name"] == data["last_name"]
    assert content["email"] == data["email"]
    assert response.status_code == 200
    
@pytest.mark.django_db
def test_put_admin_400(admin_client):
    user = User.objects.create_user(username="user1", password="pass1")
    user.save()
    path = f"/profiles/{user.id}"
    response = admin_client.put(path, {}, content_type="application/json")
    assert response.status_code == 400


# User tests
@pytest.mark.django_db
def test_put_user_400(client):
    """Test update your own profile with emputy data
        Result: 400 status code
    """
    user = User.objects.create_user(
        username=fk.name().split()[0],
        password=fk.password(),
    )
    user.save()
    client.force_login(user)
    
    response = client.put(f"/profiles/{user.id}", {}, content_type="application/json")
    assert response.status_code == 400
    
    
@pytest.mark.django_db
def test_put_user_200(client):
    """Test update your own profile
        Return: 200 status code
    """
    user = User.objects.create_user(username="user1", password="pass1")
    user.save()
    path = f"/profiles/{user.id}"
    client.force_login(user)
    response = client.put(path, data, content_type="application/json")
    content = response.json()
    assert content["username"] == data["username"]
    assert content["first_name"] == data["first_name"]
    assert content["last_name"] == data["last_name"]
    assert content["email"] == data["email"]
    assert response.status_code == 200

# Client tests
def test_put_client_403(client):
    response = client.put(f"/profiles/{10}", {})
    assert response.status_code == 403


@pytest.mark.django_db
def test_put_client_403(client):
    user = User.objects.create_user(
        username=fk.name().split()[0],
        password=fk.password(),
    )
    user.save()
    
    response = client.put(f"/profiles/{user.id}", {})
    assert response.status_code == 403