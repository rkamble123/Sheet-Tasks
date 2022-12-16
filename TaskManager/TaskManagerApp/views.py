from django.shortcuts import render
from django.views import View
import io
from rest_framework.parsers import JSONParser
from .models import TaskModel,SubtaskModel
from django.http import JsonResponse
from .serializers import TaskSerializer
from django.contrib.auth import login,logout,authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

# Create your views here.


class TaskApi(View):

    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            print("authenticated")
            # json_data = request.body
            # stream = io.BytesIO(json_data)
            # parsed_data = JSONParser().parse(stream)
            # id = parsed_data.get("id")
            task_data = TaskModel.objects.all()
            serialized_data = TaskSerializer(task_data,many=True)
            print(task_data)
            return JsonResponse(serialized_data.data,safe=False)

        else:
            print("unauthenticated")
            return JsonResponse({"msg":"Unauthenticated User Kindly Log In First !!!"},safe=False)


    def post(self,request):
        if request.user.is_authenticated:
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            serialized_data = TaskSerializer(serialized_data)
            if serialized_data.is_valid():
                serialized_data.save()
                return JsonResponse({'msg':'Task Created'},safe=False)
            return JsonResponse({'msg':'Invalid Data'},safe=False)
            
        return JsonResponse({"msg":"Unauthenticated User Kindly Log In First !!!"},safe=False)

 




class SubtaskApi(View):

    def get(self,request):

        if request.user.is_authenticated:
            print("authenticated")
            # json_data = request.body
            # stream = io.BytesIO(json_data)
            # parsed_data = JSONParser().parse(stream)
            # id = parsed_data.get("id")
            task_data = SubtaskModel.objects.all()
            serialized_data = SubtaskModel(task_data,many=True)
            print(task_data)
            return JsonResponse(serialized_data.data,safe=False)

        else:
            print("unauthenticated")
            return JsonResponse({"msg":"Unauthenticated User Kindly Log In First !!!"},safe=False)

    def post(self,request):

        pass


@csrf_exempt
def log_in(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        parsed_data = JSONParser().parse(stream)
        if parsed_data.get('user_name') and parsed_data.get("password"):
            u_name = parsed_data.get('user_name')
            u_password = parsed_data.get('password')
            user = authenticate(username = u_name,password = u_password)
            if user is not None:
                login(request,user)
                return JsonResponse({'msg':"Logged In Succesfully !!!"},safe=False)
            return JsonResponse({'msg':"Wromg User name or password !!!"},safe=False)


def log_out(request):
    if request.method == "GET":
        print('You are in get of log_out')
        logout(request)
        return JsonResponse({'msg':"Logged Out Succesfully !!!"},safe=False)
    
                        
@csrf_exempt
def UserCreation(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        parsed_data = JSONParser().parse(stream)
        u_name = parsed_data.get("username")
        u_password = parsed_data.get("password")
        try:
            User.objects.create_user(username=u_name,password=u_password)
        except Exception as e:
            return JsonResponse({'msg':f'{e}'},safe=False)
        else:
            return JsonResponse({'msg':'Account Created !!!'},safe=False)

