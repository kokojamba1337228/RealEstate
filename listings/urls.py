from django.urls import path

from . import views

urlpatterns = [
    path("/home", views.home, name="home"),
    path("sign-up/", views.sign_up, name="signup"),
    path("log-in/", views.log_in, name="login"),
]