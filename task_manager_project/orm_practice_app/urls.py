from django.urls import path
from orm_practice_app import views


urlpatterns = [
    path('',views.home,name='orm'),
]