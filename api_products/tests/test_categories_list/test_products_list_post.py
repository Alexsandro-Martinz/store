import pytest
from api_products.models import Category
from rest_framework import status
from datetime import datetime


def test_post_admin_200(admin_client):
    data = {
        'product_name':'carne de boi',
        'description': 'carne bovina',
        'expire_date': datetime.now().date(),
        'units': 500,
        'category': ''
    }
    response = admin_client.post('/products/', data=data)
    assert response.status_code == status.HTTP_201_CREATED

def test_post_admin_400(admin_client):
    response = admin_client.post('/products/', data={})
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_post_client_403(client):
    response = client.post('/products/', data={})
    assert response.status_code == status.HTTP_403_FORBIDDEN