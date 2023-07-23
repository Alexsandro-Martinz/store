from django.urls import path
from api_products import views

urlpatterns = [
    path('categories/', view=views.CategoriesList.as_view(), name='categories_list'),
    path('categories/<int:pk>/', view=views.CategoriesDetail.as_view(), name="categories_detail"),
    
    path('products/', view=views.ProductsList.as_view(), name='products_list'),
    path('products/<int:pk>/', view=views.ProductsDetail.as_view(), name="products_detail"),
]
