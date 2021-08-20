from django.http.response import JsonResponse
from rest_framework.response import Response
from .models import Product
from . import serializers
from .serializers import ProductModelSerializer
from rest_framework.parsers import JSONParser
import io
from rest_framework.decorators import api_view


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'list': '/product-list/',
        'create': '/product-create/',
        'detail': '/product-detail/<str:pk>',
        'delete': '/remove-product/<str:pk>',
        'update': '/update-product/str:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
def read(request):
        products = Product.objects.all()
        serializer = ProductModelSerializer(products, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def detail(request, pk):
    if request.method == "GET":
        products = Product.objects.get(id=pk)
        serializer = ProductModelSerializer(products, many=Frue)
        return Response(serializer.data)

@api_view(['POST'])
def create(request):
    serializer = ProductModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {'Success': 'Data Created'}
        return Response(message)
    else:    
        return Response(serializer.errors)    


@api_view(['POST'])
def create(request):
    serializer = ProductModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {'Success': 'Data Created'}
        return Response(message)
    else:    
        return Response(serializer.errors)    

@api_view(['POST'])
def update(request, pk):
    products = Product.object.get(id=pk)
    serializer = ProductModelSerializer(instance=Product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {'Success': 'Data Created'}
        return Response(message)
    else:    
        return Response(serializer.errors)    
