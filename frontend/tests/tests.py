from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import reverse
from faker import Faker


class TestLogin(TestCase):
    
    def test_authentication_true(self):
        fake = Faker()
        newUser = User.objects.create_user(fake.name(), fake.email(), fake.password())
        
        
        self.assertIsNotNone(User.objects.get(pk=newUser.id))
        self.assertEqual(newUser, User.objects.get(pk=newUser.id))
    
    def test_login_with_valid_crendentials(self):
        f = Faker()
        username = f.name()
        password = f.password()
        
        User.objects.create_user(username=username, email=f.email(), password=password)
        
        response = self.client.post('/', {'username':username, 'password': password},)

        self.assertEqual(response.status_code, 302)
        
    def test_login_with_invalid_crendentials(self):
        fake = Faker()
        response = self.client.post('/', {
            'username': fake.name(),
            'password': fake.password(),
        })
        
        messageError = "Error when logging in the user.Try again."

        self.assertContains(response, messageError)
