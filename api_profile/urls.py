from django.urls import path

from api_profile import views


urlpatterns = [
    path('', views.ListProfiles.as_view(), name="list_profiles"),
]
