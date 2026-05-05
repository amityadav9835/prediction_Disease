from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout_view, name="logout"),
    path("diabetes/", views.diabetes, name="diabetes"),
    path("parkinsons/", views.parkinsons, name="parkinsons"),
    path("heartdisease/", views.heartdisease, name="heartdisease"),
]
