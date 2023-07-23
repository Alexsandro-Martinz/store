import json
import pytest
from api_products.serializers import CategorySerializer
from rest_framework import status


# Admin tests
@pytest.mark.django_db
def test_post_admin_201(admin_client):
    response = admin_client.post('/categories/', data={'category_name': 'carne'})
    assert response.status_code == status.HTTP_201_CREATED
    
    content = response.json()
    assert content['category_name'] == 'carne'
    assert content['id'] is not None
    

@pytest.mark.django_db
def test_post_admin_400(admin_client):
    response = admin_client.post('/categories/', {'category_name': ''})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    admin_client.post('/categories/', {'category_name': 'carne'})
    response = admin_client.post('/categories/', {'category_name': 'carne'})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    
# User tests
@pytest.mark.django_db
def test_post_user_201(client, django_user_model):
    user = django_user_model.objects.create_user(
        username = "user1",
        password= 'passw1'
    )
    user.save()
    client.force_login(user)
    response = client.post('/categories/', {'category_name': 'carne'})
    assert response.status_code == status.HTTP_201_CREATED
    content = response.json()
    assert content['category_name'] == 'carne'
    assert content['id'] is not None
    
# Client tests
@pytest.mark.django_db
def test_post_client_403(client):
    response = client.post('/categories/', {'category_name': 'carne'})
    content = json.loads(response.content)
    assert response.status_code == status.HTTP_403_FORBIDDEN