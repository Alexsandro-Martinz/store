import json
from faker import Faker
from django.contrib.auth.models import User
from api_profile.serializers import UserSerializer


fake = Faker()

def test_get_profile_unauthorized(client):
    response = client.get("/profiles/1")
    assert response.status_code == 403


def test_get_profile_status_code_200(admin_client):
    user = User.objects.create_user(
        username=fake.name().split()[1],
        password=fake.password())
    
    serialized = UserSerializer(user).data
    
    response = admin_client.get('/profiles/'+str(user.id))
    content = json.loads(response.content)
    assert response.status_code == 200
    assert serialized == content

def test_object_not_founded_404(admin_client):
    response = admin_client.get('/profiles/10846')
    assert response.status_code == 404