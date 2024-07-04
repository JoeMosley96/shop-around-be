from rest_framework import viewsets
from .models import Products, Stores, PriceReport, Favorite_Products, Users
from .serializers import ProductsSerializer, StoresSerializer, PriceReportSerializer, FavouriteProductsSerializer, UsersSerializer
from django.http import JsonResponse
import importlib.resources
from .queries import get_local_prices
import json

def index(request):
    with importlib.resources.open_text("api", "endpoints.json") as file:
        data = json.load(file)

    return JsonResponse(data)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class StoresViewSet(viewsets.ModelViewSet):
    queryset = Stores.objects.all()
    serializer_class = StoresSerializer

class PriceReportViewSet(viewsets.ModelViewSet):
    queryset = PriceReport.objects.all()
    serializer_class = PriceReportSerializer

class FavouriteProductsViewSet(viewsets.ModelViewSet):
    queryset = Favorite_Products.objects.all()
    serializer_class = FavouriteProductsSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

def price_report(request, product_id, lat, lon, rad):
    price_report = get_local_prices(product_id, lat, lon, rad)
    return JsonResponse(price_report, safe=False)


