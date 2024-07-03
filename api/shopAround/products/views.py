from rest_framework import viewsets
from .models import Products
from .serializers import ProductsSerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer