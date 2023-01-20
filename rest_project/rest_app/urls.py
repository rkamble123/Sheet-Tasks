from django.urls import path
from . import views


urlpatterns = [
    
    # Function Based

    # product
    path('product_api/',views.product_api,name='product_api'),
    path('Uproduct_api/<int:pk>',views.product_api,name='product_api'),
    # category
    path('category_list_create_api',views.category_list_create_api,name='category_list_create_api'),
    path('category_detail_udpate_api/<int:pk>',views.category_detail_udpate_api,name='category_detail_udpate_api'),


    # Class Based

    # product
    path('ProductListCreateApi',views.ProductListCreateApi.as_view(),name='ProductListCreateApi'),
    path('ProductDetailUpdateApi/<int:pk>',views.ProductDetailUpdateApi.as_view(),name='ProductDetailUpdateApi'),
    # path('ProductApi/',views.ProductApi.as_view(),name='ProductApi')

    # category
    path('CategoryListCreateApi',views.CategoryListCreateApi.as_view(),name='CategoryListCreateApi'),
    path('CategoryDetailUpdateApi/<int:pk>',views.CategoryDetailUpdateApi.as_view(),name='CategoryDetailUpdateApi'),


    # Generic Api View
    path('ListCreateProduct',views.ListCreateProduct.as_view(),name='ListCreateProduct'),
    path('RetriveUpdateDeleteProduct/<int:pk>',views.RetriveUpdateDeleteProduct.as_view(),name='RetriveUpdateDeleteProduct'),


]