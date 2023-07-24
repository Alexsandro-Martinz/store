import pytest
from api_products.models import Product
from rest_framework import status
from datetime import datetime

def create_product():
    product = Product.objects.create(
        product_name = 'carne de boi',
        description = 'carne bovina',
        expire_date = datetime.now().date(),
        units = 500,
    )
    product.save()
    return product

@pytest.mark.django_db
def test_delete_admin_204(admin_client):
    product = create_product()
    response = admin_client.delete(f'/products/{product.id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Product.objects.all().count() == 0

@pytest.mark.django_db
def test_delete_admin_404(admin_client):
    product = create_product()
    response = admin_client.delete(f'/products/{23}/')
    assert response.status_code == status.HTTP_404_NOT_FOUND