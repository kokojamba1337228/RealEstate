from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("adv/", views.property_add, name="property_add"),
    path("sign-up/", views.sign_up, name="signup"),
    path("log-in/", views.log_in, name="login"),
]