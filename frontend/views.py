from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import View


@login_required
def productsView(request):
    return render(request, "frontend/products.html")

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse("frontend:home"))

        return render(request, "frontend/login.html")

    def post(self, request):
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
    return render(request, 'frontend/accounts.html')