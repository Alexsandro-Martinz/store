import pytest
from api_products.models import Category
from rest_framework import status

def create_category(category_name: str):
    category = Category.objects.create(category_name=category_name)
    category.save()
    return category

@pytest.mark.django_db
def test_delete_admin_204(admin_client):
    category = create_category('frutas')
    response = admin_client.delete(f'/categories/{category.id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Category.objects.all().count() == 0

def test_delete_admin_404(admin_client):
    category = create_category('frutas')
    response = admin_client.delete(f'/categories/{23}/')
    assert response.status_code == status.HTTP_404_NOT_FOUND