from rest_framework import serializers
from .models import Products, Stores, PriceReport, Favorite_Products, Users

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"
        
class StoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stores
        fields = "__all__"

class PriceReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceReport
        fields = "__all__"

class FavouriteProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite_Products
        fields = "__all__"

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"