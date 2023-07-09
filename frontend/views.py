from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def loginView(request):
    if request.user.is_authenticated:
        return redirect(reverse('frontend:home'))

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse('frontend:home'))
        else:
            messages.add_message(request, messages.ERROR, "Error when logging in the user.Try again.")
            messages.get_messages(request).used = True

    return render(request, "frontend/login.html")

@login_required
def homeView(request):
   return render(request, "frontend/index.html")


def logoutView(request):
    logout(request)
    return redirect(reverse('frontend:login'))