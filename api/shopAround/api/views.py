from rest_framework import viewsets
from .models import Products, Stores, PriceReport, Favorite_Products, Users, Categories
from .serializers import ProductsSerializer, StoresSerializer, PriceReportSerializer, FavouriteProductsSerializer, UsersSerializer, CategoriesSerializer
from django.http import JsonResponse
import importlib.resources
from .queries import get_local_prices, get_local_stores, get_favourites_by_user, get_products_by_category_id, check_category_id, check_user_id, check_product_id
import json
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

def index(request):
    with importlib.resources.open_text("api", "endpoints.json") as file:
        data = json.load(file)

    return JsonResponse(data)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def retrieve(self, request, pk=None):
        try:
            product = get_object_or_404(self.queryset, pk=pk)
            serializer = self.get_serializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Http404:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class StoresViewSet(viewsets.ModelViewSet):
    queryset = Stores.objects.all()
    serializer_class = StoresSerializer

    def retrieve(self, request, pk=None):
        try:
            stores = get_object_or_404(self.queryset, pk=pk)
            serializer = self.get_serializer(stores)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Http404:
            return Response({"error": "Store not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    

class PriceReportViewSet(viewsets.ModelViewSet):
    queryset = PriceReport.objects.all()
    serializer_class = PriceReportSerializer
    def retrieve(self, request, pk=None):
        try:
            price_report = get_object_or_404(self.queryset, pk=pk)
            serializer = self.get_serializer(price_report)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Http404:
            return Response({"error": "Price report not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class FavouriteProductsViewSet(viewsets.ModelViewSet):
    queryset = Favorite_Products.objects.all()
    serializer_class = FavouriteProductsSerializer
def retrieve(self, request, pk=None):
        try:
            favourites = get_object_or_404(self.queryset, pk=pk)
            serializer = self.get_serializer(favourites)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Http404:
            return Response({"error": "Favourite not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
def retrieve(self, request, pk=None):
        try:
            user = get_object_or_404(self.queryset, pk=pk)
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Http404:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
def retrieve(self, request, pk=None):
        try:
            categories = get_object_or_404(self.queryset, pk=pk)
            serializer = self.get_serializer(categories)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Http404:
            return Response({"error": "Categories not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def price_report(request, product_id, lat, lon, rad):
    price_report = get_local_prices(product_id, lat, lon, rad)
    product_exists = check_product_id(product_id)
    if(product_exists == True):
        return JsonResponse(price_report, safe=False)
    else:
        return JsonResponse({'error': 'Product not found'}, status=404)

def local_stores(request, lat, lon):
    try:
        rad = float(request.GET.get('rad', 1000))
    except:
        return JsonResponse({'error': 'radi should be an integer'}, status=400)
    
    stores_reports = get_local_stores(lat, lon, rad)
    return JsonResponse(stores_reports, safe=False)

def favourites (request, user_id):
    favourite_products_by_user = get_favourites_by_user(user_id)
    user_exists = check_user_id(user_id)
    if(user_exists == True):
        return JsonResponse(favourite_products_by_user, safe=False)
    else:
        return JsonResponse({'error': 'User not found'}, status=404)

def products_by_category(request, category_id):
    products_by_category_id = get_products_by_category_id(category_id)
    category_exists = check_category_id(category_id)
    if(category_exists == True):
        return JsonResponse(products_by_category_id, safe=False)
    else:
        return JsonResponse({'error': 'Category not found'}, status=404)