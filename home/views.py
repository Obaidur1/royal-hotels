from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import RoyalHotelModel, User_Reviews
from django.db.models import Q


# Create your views here.
def home(request):
    query = request.GET.get("search", "")
    hotels = None
    if query:
        hotels = RoyalHotelModel.objects.filter(Q(address__icontains=query))
    else:
        hotels = RoyalHotelModel.objects.all()
    return render(request, "index.html", {"hotels": hotels})


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "login.html", {"error": "Invalid login credentials"})
    return render(request, "login.html")


def user_registration(request):
    error = None
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 != password2:
            error = "Passwords not matched"
        else:
            try:
                User.objects.create_user(
                    username=username, email=email, password=password1
                )
                return redirect("login")
            except Exception as e:
                error = str(e)
    return render(request, "registration.html", {"error": error})


def user_logout(request):
    logout(request)
    return redirect("home")


def hotel_details(request, id):
    hotel = get_object_or_404(RoyalHotelModel, pk=id)
    reviews = User_Reviews.objects.filter(hotel=hotel)
    print(reviews)
    return render(request, "hotel_detail.html", {"hotel": hotel, "reviews": reviews})
