from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import View
from frontend.forms import AddProductForm

from frontend.models import Category, Product


@login_required
def productsView(request):
    context = {"categories": Category.objects.all()}
    return render(request, "frontend/products/products.html", context)


@login_required
def addProductsView(request):
    if request.method == "POST":
        add_product_form = AddProductForm(request)
        if add_product_form.is_valid():
            
            Product.objects.create(
                product_name=add_product_form.cleaned_data["product_name"],
                description=add_product_form.cleaned_data['description'],
                category_id=add_product_form.cleaned_data['category_id'],
                expire_date=add_product_form.cleaned_data['expire_date'],
                units=add_product_form.cleaned_data['units'],
            ).save()
            

    template_name = "frontend/products/add-products.html"
    context = {"categories": Category.objects.all()}
    return render(request, template_name, context)


def loginView(request):
    if request.user.is_authenticated:
        return redirect(reverse("frontend:home"))

    if request.method == "POST":
        user = authenticate(
            username=request.POST["username"], password=request.POST["password"]
        )

        if user is not None:
            login(request, user)
            return redirect(reverse("frontend:home"))
        else:
            messages.add_message(
                request, messages.ERROR, "Error when logging in the user.Try again."
            )
            messages.get_messages(request).used = True

    return render(request, "frontend/login.html")


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
