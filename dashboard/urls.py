from django.urls import path
from dashboard.views import dashboard, profile_update, password_change

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("profile", profile_update, name="profile_update"),
    path("change-password", password_change, name="change_password"),
]
