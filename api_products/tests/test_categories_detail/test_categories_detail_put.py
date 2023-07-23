import pytest
from api_products.models import Category
from rest_framework import status


def create_category(category_name: str):
    category = Category.objects.create(category_name=category_name)
    category.save()
    return category


def test_put_admin_200(admin_client):
    category = create_category("massas")
    new_category_name = "laticinios"
    data = {"category_name": new_category_name}
    response = admin_client.put(
        f"/categories/{category.id}/", data=data, content_type="application/json"
    )
    content = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert content['category_name'] == new_category_name
    assert content['id'] != None

def test_put_admin_404(admin_client):
    data = {"category_name": "carne"}
    response = admin_client.put(
        f"/categories/{30}/", data=data, content_type="application/json"
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_put_admin_400(admin_client):
    category = create_category("massas")
    data = {}
    response = admin_client.put(
        f"/categories/{category.id}/", data=data, content_type="application/json"
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_put_client_400(client):
    category = create_category("massas")
    data = {}
    response = client.put(
        f"/categories/{category.id}/", data=data, content_type="application/json"
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN