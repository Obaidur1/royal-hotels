from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import UpdateUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from home.models import User_Reviews

# from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages


# Create your views here.
@login_required(login_url="login")
def dashboard(request):
    return render(request, "dashboard.html")


@login_required(login_url="login")
def profile_update(request):
    if request.method == "POST":
        form = UpdateUser(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile_update")
    else:
        form = UpdateUser(instance=request.user)
    return render(request, "profile.html", {"form": form})


@login_required(login_url="login")
def password_change(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, "change-password.html", {"form": form})


@login_required(login_url="login")
def my_reviews(request):
    user = request.user
    reviews = User_Reviews.objects.filter(user=user)
    return render(request, "my_reviews.html", {"reviews": reviews})
