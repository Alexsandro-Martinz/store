from django.urls import path

from api_profile import views


urlpatterns = [
    path('', views.ProfilesViewList.as_view(),name="profiles-view-list"),
    path('<int:pk>', views.ProfilesView.as_view(),name="profiles-view"),
]
