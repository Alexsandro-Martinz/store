from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from frontend.models import Category


@login_required
def productsView(request):
    context = {"categories": Category.objects.all()}
    return render(request, "frontend/products/products.html", context)
