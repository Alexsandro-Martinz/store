import pytest
from rest_framework import status
from api_products.models import Product, Category

data = {
    "product_name": "banana",
    "units": 390,
    "expire_date": "2022-12-28",
    "category_id": "",
    "description": "é um fruta of course",
}


# Admin tests
@pytest.mark.django_db
def test_get_admin_200(admin_client):
    pass


# User tests


# Client test
def test_get_client_403(client):
    response = client.get("/products/")
    assert response.status_code == status.HTTP_403_FORBIDDEN
