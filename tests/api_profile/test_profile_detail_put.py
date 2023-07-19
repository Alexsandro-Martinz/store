import json
from faker import Faker
from django.contrib.auth.models import User
import pytest
from api_profile.serializers import UserSerializer


fk = Faker()

@pytest.mark.django_db
def test_put_admin(admin_client):
    user = User.objects.create_user(
        username="user1",
        password="pass1"
    )
    user.save()
    path = f'/profiles/{user.id}'
    data = {
        "username": "user2",
        'first_name': str(fk.name().split()[0]),
        'last_name': str(fk.name().split()[-1]),
        'email': str(fk.email()),
        'password': str(fk.password()),
    }
    
    response = admin_client.patch(path, data, content_type="application/json")
    content = json.loads(response.content.decode())
    assert content['username'] == data['username']
    assert content['first_name'] == data['first_name']
    assert content['last_name'] == data['last_name']
    assert content['email'] == data['email']
    assert response.status_code == 200
    