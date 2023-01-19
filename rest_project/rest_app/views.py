from django.shortcuts import render
from .serializers import ProductSerializer
from rest_app.models import products,categories
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from rest_framework import status

# Create your views here.

@api_view(['GET','POST',"PUT",'PATCH',"DELETE"])
def product_api(request,pk=None):
    if request.method == 'GET':
        if pk:
            product_data = products.objects.get(id=pk)
            serializer = ProductSerializer(product_data)
            return Response(serializer.data)        
        product_data = products.objects.all()
        print(product_data)
        serializer = ProductSerializer(product_data,many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Msg':'Data Created.'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        product_data = products.objects.get(id=pk)
        serializer = ProductSerializer(product_data,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Msg':"Data Updated."},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        product_data = products.objects.get(id=pk)
        serializer = ProductSerializer(product_data,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Msg':"Data Updated."},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        product_data = products.objects.get(id=pk)
        product_data.delete()
        return Response({'Msg':"Data Deleted."},status=status.HTTP_204_NO_CONTENT)
        



class ProductApi(APIView):
    def get(self,request,format=None):
        product_data = products.objects.get(id=1)
        print(product_data)
        serializer = ProductSerializer(product_data)
        return Response(serializer.data)

