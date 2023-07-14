from django.test import TestCase
from django.contrib.auth.models import User
from faker import Faker
import pytest

@pytest.mark.django_db
class TestLogin:

    def test_authentication_true(self):
        fake = Faker()
        newUser = User.objects.create_user(fake.name(), fake.email(), fake.password())
        
        assert User.objects.get(pk=newUser.id) != None
        assert newUser == User.objects.get(pk=newUser.id)
    
    def test_login_with_valid_crendentials(self, client):
        f = Faker()
        username = f.name()
        password = f.password()
        
        User.objects.create_user(username=username, email=f.email(), password=password)
        
        response = client.post('/', {'username':username, 'password': password},)

        assert response.status_code == 302
        
    def test_login_with_invalid_crendentials(self, client):
        fake = Faker()
        response = client.post('/', {
            'username': fake.name(),
            'password': fake.password(),
        })
        
        messageError = "Error when logging in the user.Try again."

        assert messageError.encode() in response.content
