from django.urls import path

from api_profile import views


urlpatterns = [
    path('', views.list_profiles, name="list_profiles"),
]
