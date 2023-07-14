from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import View
from frontend.forms import AddProductForm

from frontend.models import Category, Product


@login_required
def delProduct(request) :
    data = {}
    if request.accepts('application/json') and request.method == 'POST':
        id = request.POST['id']
        get_object_or_404(Product, pk=id).delete()
        data['messageSuccess'] = 'Deleted with success!'
    
    return JsonResponse(data, status=200)

@login_required
def delCategory(request) :
    data = {}
    if request.accepts('application/json') and request.method == 'POST':
        id = request.POST['id']
        get_object_or_404(Category, pk=id).delete()
        data['messageSuccess'] = 'Deleted with success!'
    
    return JsonResponse(data, status=200)

@login_required
def addCategory(request):
    data = {}
    if request.accepts('application/json') and request.method == 'POST':
        category_name = request.POST['category_name']
        ct = Category.objects.create(category_name=category_name)
        ct.save()
        data['messageSuccess'] = ct.category_name.upper() + 'saved with success!'
    
    return JsonResponse(data, status=200)

@login_required
def productsView(request):
    context = {
        "categories": Category.objects.all(),
        "products": Product.objects.all(),}
    return render(request, "frontend/products/products.html", context)


@login_required
def addProductsView(request):
    context = {}
    if request.method == "POST":

        add_product_form = AddProductForm(request.POST)
        
        if add_product_form.is_valid():            
            
            expired_date_str = add_product_form.cleaned_data['expire_date']
            expire_date = datetime.strptime(expired_date_str, '%Y-%m-%d').date()
            product_add = Product.objects.create(
                product_name=add_product_form.cleaned_data["product_name"],
                description=add_product_form.cleaned_data['description'],
                category_id=add_product_form.cleaned_data['category_id'],
                expire_date=expire_date,
                units=add_product_form.cleaned_data['units'],
            )
            product_add.save()
            context['product_add'] = product_add
      
            
    template_name = "frontend/products/add-products.html"
    context = {
        "categories": Category.objects.all(),
        'products': Product.objects.all(),}
    return render(request, template_name, context)

@login_required
def homeView(request):
    return render(request, "frontend/home.html")


@login_required
def logoutView(request):
    logout(request)
    return redirect(reverse("frontend:login"))


@login_required
def accountsView(request):
    return render(request, "frontend/accounts.html")
