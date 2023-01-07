from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import TaskModel,SubtaskModel

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Enter The Username : ',widget=forms.TextInput(attrs={'class':'form-control'}))
    password  = forms.CharField(label = 'Enter The Passowrd : ',widget = forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','password']


class SubTaskForm(forms.ModelForm):

    class Meta:
        model = SubtaskModel
        fields = ['sub_task_name','task_id']
        label = {
            'sub_task_name' : "Enter The Sub Task Name : ",
        }

        widgets = {
            'sub_task_name' : forms.TextInput(attrs={'class':'form-control'}),
            'task_id': forms.TextInput(attrs={'class':'form-control'})            
        }


# class TaskForm(forms.ModelForm):

#     class Meta:
#         model = TaskModel
#         fields = ['task_name','status','owner']
#         label = {
#             'task_name': 'Task Name',
#             'status' : 'Status',
#             # 'owner':'Owner'
#         }

#         widgets = {

#             'task_name' : forms.TextInput(attrs={'class':'form-control'}),
#             'status' : forms.

#         }