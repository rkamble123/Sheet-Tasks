from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import login, logout, authenticate
from .models import TaskModel, SubtaskModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SubTaskForm, TaskForm, Registerform
from django.core.paginator import Paginator 

# Create your views here.


def home(request,*args,**kwargs):
    print(request.GET.get('user'))
    print(request.GET.get('user2'))


    # get_query_params = request.query_params.get('status',None)
    # if get_query_params:
    #     param = get_query_params
    # param=''

    return render(request, "home.html")


def register_user(request):
    if request.method == 'GET':
        form = Registerform()
        return render(request, 'register_user.html', {'form': form})
    if request.method == 'POST':
        form = Registerform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User Registered !!!')
            return redirect('home')


def log_in(request):
    if request.method == 'GET':
        log_in_form = LoginForm
        return render(request, 'log_in.html', {'form': log_in_form})
    if request.method == 'POST':
        form = LoginForm(request.POST, data=request.POST)
        if form.is_valid():
            print('form is valid.')
            u_name = form.cleaned_data['username']
            u_pass = form.cleaned_data['password']
            print(u_name)
            print(u_pass)
            user = authenticate(username=u_name, password=u_pass)
            if user is not None:
                login(request, user)
                messages.success(request, 'Log In Successful !!!')
                return redirect('user_task_list')
            messages.warning(request, "Invalid Username or Password !!!")
            return redirect('log_in')
        messages.warning(request, 'Invalid Username or Password !!!')
        return redirect('log_in')


@login_required(login_url='http://127.0.0.1:8000/log_in')
def user_task_list(request,*args,**kwargs):

    # print(request.headers)
    if request.method == "GET":
        if request.user.is_authenticated:
            data = TaskModel.objects.filter(owner_id=request.user.id)

            status = request.GET.get('status')
            print(status)
            if status :
                if status != 'None':
                    data = data.filter(status=status)

            task_paginator = Paginator(data,5)
            
            page_no = request.GET.get('page_no',1)
            
            data = task_paginator.get_page(page_no)

            task = TaskModel(request).StatusChoices
            return render(request, 'user_task_list.html', {'data': data,'status_choice':task,'status':status})
        messages.warning(request, "No Permission Login First !!!")
        return redirect('log_in')


def log_out(request):
    # if request.method == "GET":
    logout(request)
    messages.warning(request, 'Logged Out Succesfully !!!')
    return redirect('home')


@login_required(login_url='http://127.0.0.1:8000/log_in')
def task_details(request, pk):

    Task_data = TaskModel.objects.get(id=pk)
    Sub_task_data = SubtaskModel.objects.filter(task_id=pk)

    init_dict = {
        'task': Task_data
    }
    form = SubTaskForm(initial=init_dict)

    if request.method == 'POST':
        sub_task_form = SubTaskForm(request.POST, initial=init_dict)

        if sub_task_form.is_valid():
            sub_task_form.save()
            return redirect("task_details", pk)

    return render(
        request,
        'task_details.html',
        {
            'Task_data': Task_data,
            'Sub_task_data': Sub_task_data,
            'form': form
        }
    )


@login_required(login_url='http://127.0.0.1:8000/log_in')
def create_task(request):
    if request.method == "GET":
        form = TaskForm(request)
        return render(request, 'create_task.html', {'form': form})
    if request.method == 'POST':
        form = TaskForm(request, request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_task_list')


def delete_task(request, pk):
    if request.method == "GET":
        data = TaskModel.objects.get(id=pk)
        print(data)
        data.delete()
        messages.success(request, 'Task Deleted Succesfully !!!')
        return redirect('user_task_list')


def about_us(request):
    return render(request, 'about.html')


def contact_us(request):
    return render(request, 'contact_us.html')
