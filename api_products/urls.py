from django.urls import path
from api_products import views

urlpatterns = [
    path('categories/', view=views.categories_list, name='categories_list'),
    path('categories/<int:pk>/', view=views.categories_detail, name="categories_detail"),
    
    path('products/', view=views.products_list, name='products_list'),
    path('products/<int:pk>/', view=views.products_detail, name="products_detail"),
]
