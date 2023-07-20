from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse
from django.views import View


class LoginView(View):
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse("frontend:home"))
        return render(request, "frontend/login.html")

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse("frontend:home"))

        messages.add_message(
            request, messages.ERROR, "Error when logging in the user.Try again."
        )
        messages.get_messages(request).used = True
        return render(request, "frontend/login.html")


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
