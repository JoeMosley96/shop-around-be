from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, StoresViewSet, PriceReportViewSet, FavouriteProductsViewSet, UsersViewSet

from . import views

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'stores', StoresViewSet)
router.register(r'prices', PriceReportViewSet)
router.register(r'favourites', FavouriteProductsViewSet)
router.register(r'users', UsersViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path("products/", include("products.urls")),
    path('', views.index, name="index"),
]