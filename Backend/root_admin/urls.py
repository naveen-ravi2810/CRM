from django.urls import path
from .views import login, register, get_profile, update_admin

urlpatterns = [
    path("login", login, name="Login User"),
    path("register", register, name="Register User"),
    path("profile", get_profile, name="Get the admin profile"),
    path("update", update_admin, name="Update the Admin Profile"),
]
