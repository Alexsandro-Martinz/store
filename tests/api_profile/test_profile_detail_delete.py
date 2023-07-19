"""
    These are the tests for method delete to endpoint '/profiles/id/'
    Patterns to write a name method
        : def test method status_code type_client 
        - Example:
            def test_delete_204_admin():
"""

import pytest
from faker import Faker
from django.contrib.auth.models import User
from api_profile.serializers import UserSerializer

fk = Faker()
username: str = fk.name()[0]
password: str = fk.password()

# Admin tests
@pytest.mark.django_db
def test_delete_admin_204(admin_client):
    """
    Test delete any user by admin
    Return: 204 status code
    """
    user = User.objects.create_user(username=username, password=password)
    user.save()
    response = admin_client.delete(f"/profiles/{user.id}")
    amount = User.objects.all().count()
    assert response.status_code == 204
    assert amount == 1


@pytest.mark.django_db
def test_delete_admin_404(admin_client):
    """
    Test tries to delete user not register by admin
    Return: 404 status code
    """
    response = admin_client.delete(f"/profiles/{15}")
    amount = User.objects.all().count()
    assert response.status_code == 404
    assert amount == 1


# Client tests
@pytest.mark.django_db
def test_delete_client_403(client):
    """
    Test client tries to delele any user
    Return: 404 status code
    """
    user = User.objects.create_user(username=username, password=password)
    user.save()
    response = client.delete(f"/profiles/{user.id}")
    amount = User.objects.all().count()
    assert response.status_code == 403
    assert amount == 1

# User tests
@pytest.mark.django_db
def test_delete_user_403(client):
    """
    Test client tries to delele any user
    Return: 404 status code
    """
    user = User.objects.create_user(username=username, password=password)
    user.save()
    client.force_login(user)
    response = client.delete(f"/profiles/{user.id}")
    amount = User.objects.all().count()
    assert response.status_code == 403
    assert amount == 1
