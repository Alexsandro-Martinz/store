import pytest
from api_products.models import Category
from rest_framework import status

def create_category(category_name: str):
    category = Category.objects.create(category_name=category_name)
    category.save()
    return category

@pytest.mark.django_db
def test_get_admin_200(admin_client):
    category = create_category('carne')
    response = admin_client.get(f'/categories/{category.id}/')
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_get_admin_400(admin_client):
    response = admin_client.get(f'/categories/{100}/')
    assert response.status_code == status.HTTP_404_NOT_FOUND
