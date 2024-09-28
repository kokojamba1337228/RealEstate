from django.contrib import admin
from django.urls import include, path
from listings import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("listings.urls")),
]
