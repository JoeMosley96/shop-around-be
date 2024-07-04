from django.urls import path, include, register_converter
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, StoresViewSet, PriceReportViewSet, FavouriteProductsViewSet, UsersViewSet
from .converters import FloatConverter
from . import views

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'stores', StoresViewSet)
router.register(r'prices', PriceReportViewSet)
router.register(r'favourites', FavouriteProductsViewSet)
router.register(r'users', UsersViewSet)

register_converter(FloatConverter, 'float')

urlpatterns = [
    path('', include(router.urls)),
    path('', views.index, name="index"),
    path('price-report/<int:product_id>/<float:lat>/<float:lon>/<int:rad>/', views.price_report, name='price_report'),
]