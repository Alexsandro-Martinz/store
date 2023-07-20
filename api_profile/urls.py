from django.urls import path

from api_profile import views


urlpatterns = [
    path('profiles/', views.profiles_list,name="profiles_list"),
    path('profiles/<int:pk>', views.profile_detail, name="profile_detail"),
]
