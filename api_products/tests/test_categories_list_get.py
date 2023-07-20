import json
import pytest
from api_products.serializers import CategorySerializer
from rest_framework import status

# Admin tests
def test_get_admin_200(admin_client):
    data = {'category_name': 'carne'}
    srz = CategorySerializer(data=data)
    category = srz.create()
    if category is None:
        raise Exception(srz.errors)
    response = admin_client.get('/categories/')
    content = json.loads(response.content)[0]
    assert response.status_code == status.HTTP_200_OK
    assert content['category_name'] == data['category_name']
    assert content['id'] is not None


# User tests
@pytest.mark.django_db
def test_get_user_200(client, django_user_model):
    user = django_user_model.objects.create_user(username='user1', password='pass1')
    client.force_login(user)
    data = {'category_name': 'carne'}
    srz = CategorySerializer(data=data)
    category = srz.create()
    if category is None:
        raise Exception(srz.errors)
    response = client.get('/categories/')
    content = json.loads(response.content)[0]
    assert response.status_code == status.HTTP_200_OK
    assert content['category_name'] == data['category_name']
    assert content['id'] is not None

# Client tests
def test_get_client_403(client):
    response = client.get('/categories/')
    assert response.status_code == status.HTTP_403_FORBIDDEN