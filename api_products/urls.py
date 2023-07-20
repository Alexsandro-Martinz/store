from django.urls import path
from api_products import views

urlpatterns = [
    path('products/', view=views.products_list, name='products_list'),
    path('products/<int:pk>/', view=views.products_detail, name="products_detail"),
]
