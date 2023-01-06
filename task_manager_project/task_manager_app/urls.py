from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.home,name ='home'),
    path('log_in',views.log_in,name='log_in'),
    path("user_task_list",views.user_task_list,name='user_task_list'),
    path("log_out",views.log_out,name='log_out'),
    # path('accounts/',include('django.contrib.auth.urls'))
    path('task_details/<int:pk>',views.task_details,name='task_details'),
    path('add_subtask/',views.add_subtask,name='add_subtask'),




]

