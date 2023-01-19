from django.urls import path
from . import views


urlpatterns = [
    path('product_api/',views.product_api,name='product_api'),
    path('Uproduct_api/<int:pk>',views.product_api,name='product_api'),
    path('ProductApi/',views.ProductApi.as_view(),name='ProductApi')

]