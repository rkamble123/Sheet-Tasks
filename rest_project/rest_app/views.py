from django.shortcuts import render
from .serializers import ProductSerializer,CategorySerializer
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


# Category Api (function based)

@api_view(["GET",'POST'])
def category_list_create_api(request,*args,**kwargs):
    if request.method == 'GET':
        product_data = categories.objects.all()
        serializer = CategorySerializer(product_data,many=True)
        return Response(serializer.data) 
    if request.method == 'POST':
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Msg':'Data Updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','PATCH','DELETE'])
def category_detail_udpate_api(request,*args,**kwargs):
    pk = kwargs.get('pk')
    if request.method == 'GET':
        product_data = categories.objects.get(id=pk)
        serializer = CategorySerializer(product_data)
        return Response(serializer.data)
    if request.method == 'PUT':
        category_data = categories.objects.get(id=pk)
        serializer = CategorySerializer(category_data,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Msg':'Data Updated'},status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PATCH':
        category_data = categories.objects.get(id=pk)
        serializer = CategorySerializer(category_data,data = request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Msg':'Data Updated'},status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        category_data = categories.objects.get(id=pk)
        category_data.delete()
        return Response({'Msg':'Data Deleted'},status=status.HTTP_204_NO_CONTENT)




# Product Api (Class Based View)

class ProductListCreateApi(APIView):

    def get(self,request,format=None):
        product_data = products.objects.all()
        print(product_data)
        serializer = ProductSerializer(product_data, many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




class ProductDetailUpdateApi(APIView):

    def get(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        print(pk)
        product_data = products.objects.get(id=pk)
        print(product_data)
        serializer = ProductSerializer(product_data)
        return Response(serializer.data)

    def put(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        product_data = products.objects.get(id=pk)
        serializer = ProductSerializer(product_data,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Msg':'Data Updated'},status=status.HTTP_201_CREATED)
        return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,*args,**kwargs):
        pk = kwargs['pk']
        product_data = products.objects.get(id=pk)
        serializer = ProductSerializer(product_data,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Msg':'Data Update'},status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_502_BAD_GATEWAY)

    def delete(self,request,*args,**kwargs):
        pk = kwargs['pk']
        product_data = products.objects.get(id=pk)
        product_data.delete()
        return Response({'Msg':'Data Deleted'},status=status.HTTP_204_NO_CONTENT)



# Category Api (Class Based View)

class CategoryListCreateApi(APIView):

    def get(self,request,*args,**kwargs):
        category_data = categories.objects.all()
        serializer = CategorySerializer(category_data,many=True)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailUpdateApi(APIView):

    def get(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        category_data = categories.objects.get(id=pk)
        serializer = CategorySerializer(category_data)
        return Response(serializer.data)
    def put(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        category_data = categories.objects.get(id=pk)
        serializer  = CategorySerializer(category_data,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Msg':'Data Updated'},status=status.HTTP_202_ACCEPTED)
        return Response({})
    def patch(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        category_data = categories.objects.get(id=pk)
        serializer  = CategorySerializer(category_data,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Msg':'Data Updated'},status=status.HTTP_202_ACCEPTED)
    def delete(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        category_data = categories.objects.get(id=pk)
        category_data.delete()
        return Response({'Msg':'Data Deleted'},status=status.HTTP_204_NO_CONTENT)







from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView



class ListCreateProduct(ListCreateAPIView):
    queryset = products.objects.all()
    serializer_class = ProductSerializer

class RetriveUpdateDeleteProduct(RetrieveUpdateDestroyAPIView):
    queryset = products.objects.all()
    serializer_class = ProductSerializer