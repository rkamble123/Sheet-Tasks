from django.urls import path
from rdb_app import views

urlpatterns = [
    path('PortalApi',views.PortalApi.as_view(),name='PortalApi'),
]