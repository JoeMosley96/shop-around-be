from rest_framework import viewsets
from .models import Products
from .serializers import ProductsSerializer
from django.http import JsonResponse
import importlib.resources
import json

def index(request):
    with importlib.resources.open_text("api", "endpoints.json") as file:
        data = json.load(file)

    return JsonResponse(data)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer