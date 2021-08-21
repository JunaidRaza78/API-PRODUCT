from django.http.response import JsonResponse
from rest_framework.response import Response
from .models import Product
from . import serializers
from .serializers import ProductModelSerializer
from rest_framework import generics


class Productlist(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product
    serializer_class = ProductModelSerializer
     