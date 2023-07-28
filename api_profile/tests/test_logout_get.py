import pytest
from rest_framework import status

@pytest.mark.djang_db
def test_get_user_200(client, django_user_model):
    
    user = django_user_model.objects.create_user(
        username = "user1",
        password = "pass2"
    )
    user.save()
    client.force_login(user)
    response = client.get('/products/')
    assert response.status_code == 200
    
    response = client.get('/logout/')
    assert response.status_code == 200    
    

def test_get_user_400(client, django_user_model):
    response = client.get('/logout/')
    assert response.status_code == status.HTTP_400_BAD_REQUEST