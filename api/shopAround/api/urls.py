from django.urls import path, include

from . import views

urlpatterns = [
    path("products/", include("products.urls")),
    path("", views.index, name="index"),
]