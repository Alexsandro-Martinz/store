from django.urls import path

from frontend.views import views
from frontend.views.loginViews import LoginView

app_name = 'frontend'

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout', views.logoutView, name='logout'),
    path('home', views.homeView, name='home'),
    path('products', views.productsView, name='products'),
    path('products/add', views.addProductsView, name='addProducts'),
    path('products/del', views.delProduct, name="delProduct"),
    path('accounts', views.accountsView, name='accounts'),
    path('categories/add', views.addCategory, name="addCategory"),
    path('categories/del', views.delCategory, name="delCategory"),
]