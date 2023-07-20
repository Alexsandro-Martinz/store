import json
import pytest
from api_products.serializers import CategorySerializer
from rest_framework import status


# Admin tests
@pytest.mark.django_db
def test_post_admin_200(admin_client):
    response = admin_client.post('/categories/', {'category_name': 'carne'})
    content = json.loads(response.content)
    assert response.status_code == status.HTTP_200_OK
    assert content['category_name'] == 'carne'
    assert content['id'] is not None
    

# User tests
@pytest.mark.django_db
def test_post_user_200(client, django_user_model):
    user = django_user_model.objects.create_user(
        username = "user1",
        password= 'passw1'
    )
    user.save()
    client.force_login(user)
    response = client.post('/categories/', {'category_name': 'carne'})
    content = json.loads(response.content)
    assert response.status_code == status.HTTP_200_OK
    assert content['category_name'] == 'carne'
    assert content['id'] is not None