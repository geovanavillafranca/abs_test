from django.shortcuts import render
from api.serializer import ClientSerializer, SellerSerializer, ProductSerializer
from api.models import Client, Seller, Product
from rest_framework import viewsets, generics

# Create your views here.


class ClientsViewSet(viewsets.ModelViewSet):
    """
        Return all clients
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class SellersViewSet(viewsets.ModelViewSet):
    """
        Return all sellers
    """
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    """
        Return all products
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
