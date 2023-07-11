from django.urls import path

from frontend import views


app_name = 'frontend'

urlpatterns = [
    path('', views.loginView, name='login'),
    path('logout', views.logoutView, name='logout'),
    path('home', views.homeView, name='home'),
    path('products', views.productsView, name='products'),
    path('products/add', views.addProductsView, name='addProducts'),
    path('accounts', views.accountsView, name='accounts'),
    path('categories/add', views.addCategory, name="addCategory"),
    path('categories/del', views.delCategory, name="delCategory"),
]