from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.home,name ='home'),
    path('log_in',views.log_in,name='log_in'),
    path("user_task_list",views.user_task_list,name='user_task_list'),
    path("log_out",views.log_out,name='log_out'),
    # path('accounts/',include('django.contrib.auth.urls'))
    path('task_details/<int:pk>',views.task_details,name='task_details'),
    # path('add_subtask/',views.add_subtask,name='add_subtask'),
    path('create_task/',views.create_task,name='create_task'),
    path('delete_task/<int:pk>',views.delete_task,name='delete_task'),
    path('register_user/',views.register_user,name='register_user'),
    path('about_us/',views.about_us,name='about_us'),
    path('contact_us/',views.contact_us,name='contact_us'),
    path('users_list/',views.users_list,name='users_list'),
    path('edit_task/<int:pk>',views.edit_task,name='edit_task'),










]

