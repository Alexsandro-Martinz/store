from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def loginView(request):
    if request.user.is_authenticated:
        print(request.user.username)
        return render(request, "frontend/index.html")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, "frontend/index.html")

    return render(request, "frontend/login.html")


def logoutView(request):
    logout(request)
    return render(request, "frontend/login.html")