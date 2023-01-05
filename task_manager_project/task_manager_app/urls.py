from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name = 'home'),
    path('log_in',views.log_in,name='log_in'),
    path("user_task_list",views.user_task_list,name='user_task_list'),
    path("log_out",views.log_out,name='log_out'),

]

