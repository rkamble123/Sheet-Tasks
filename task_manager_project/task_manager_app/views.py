from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import login,logout,authenticate
from .models import TaskModel,SubtaskModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,"home.html")

def log_in(request):
    if request.method == 'GET':
        log_in_form = LoginForm
        return render(request,'log_in.html',{'form':log_in_form})
    if request.method == 'POST':
        form = LoginForm(request.POST,data=request.POST)
        if form.is_valid():
            print('form is valid.')
            u_name = form.cleaned_data['username']
            u_pass = form.cleaned_data['password']
            print(u_name)
            print(u_pass)
            user = authenticate(username = u_name,password = u_pass)
            if user is not None:
                login(request,user)
                messages.success(request,'Log In Successful !!!')
                return redirect ('user_task_list')
            messages.warning(request,"Invalid Username or Password !!!")
            return redirect('log_in')
        messages.warning(request,'Invalid Username or Password !!!')
        return redirect('log_in')
                

@login_required
def user_task_list(request):
    if request.method == "GET":
        # if request.user.is_authenticated:
            data = TaskModel.objects.filter(owner_id = request.user.id)
            print(data)
            return render(request,'user_task_list.html',{'data':data})
        


def log_out(request):
    if request.method == "GET":
        # if request.user.is_authenticated:
            logout(request)
            messages.warning(request,'Logged Out Succesfully !!!')
            return redirect('home')
