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
def test_put_admin_200(admin_client):
    product = create_product()
    data = dict(units = 50)
    response = admin_client.put(f'/products/{product.id}/', data=data, content_type="application/json")
    assert response.status_code == status.HTTP_200_OK
    assert Product.objects.all().count() == 1

@pytest.mark.django_db
def test_put_admin_404(admin_client):
    product = create_product()
    response = admin_client.put(f'/products/{23}/')
    assert response.status_code == status.HTTP_404_NOT_FOUND