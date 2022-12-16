from django.urls import path
from . import views


urlpatterns = [
    path('log_in',views.log_in,name='log_in'),
    path('log_out/',views.log_out,name='log_out'),
    path('TaskApi/',views.TaskApi.as_view(),name="TaskApi"),
    path('SubTaskApi/',views.SubtaskApi.as_view(),name="SubTaskApi"),
    path('UserCreation/',views.UserCreation,name="UserCreation"),

]