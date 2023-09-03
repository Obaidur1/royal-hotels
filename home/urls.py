from django.urls import path
from .views import home, user_login, user_registration, user_logout, hotel_details

urlpatterns = [
    path("", home, name="home"),
    path("login", user_login, name="login"),
    path("registration", user_registration, name="registration"),
    path("logout", user_logout, name="logout"),
    path("hotel-detail/<int:id>", hotel_details, name="hotel_detail"),
]
