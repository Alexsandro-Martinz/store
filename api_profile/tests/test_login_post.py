import pytest
from api_profile.views import logoutView, loginView

@pytest.mark.djang_db
def test_post_user_200(client, django_user_model):
    
    user = django_user_model.objects.create_user(
        username = "user1",
        password = "pass2"
    )
    user.save()
    
    response = client.post('/login/', {'username':'user1','password':'pass2'})
    
    assert response.status_code == 200

def test_post_user_400(client, django_user_model):
    response = client.post('/login/', {'username':'user1','password':'pass2'})
    assert response.status_code == 400