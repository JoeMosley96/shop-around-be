from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

from . import views

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path("products/", include("products.urls")),
    path('', views.index, name="index"),
]