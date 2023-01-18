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

class Registerform(UserCreationForm):

    password1 = forms.CharField(label = 'Enter The Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label = 'Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']
        labels = {
            'first_name':'Enter The First Name ',
            'last_name':'Enter The Last Name ' ,
            'username' : 'Enter Username ',
            'email' : 'Enter The Email ',
        }   

        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
        }


class SubTaskForm(forms.ModelForm):

    class Meta:
        model = SubtaskModel
        fields = ['sub_task_name','task']
        label = {
            'sub_task_name' : "Enter The Sub Task Name : ",
            'task':'Enter The Task Name : '
        }

        widgets = {
            'sub_task_name' : forms.TextInput(attrs={'class':'form-control'}),
            'task': forms.HiddenInput(attrs={'class':'form-control', })     
        }


class TaskForm(forms.ModelForm):

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)

    class Meta:
        model = TaskModel
        fields = ['task_name','status']
        label = {
            'task_name': 'Task Name',
            'status' : 'Status',
        }

        widgets = {
            'task_name' : forms.TextInput(attrs={'class':'form-control'}),
            'status' : forms.Select(attrs={'class':'form-control'}),
        }

    def save(self, commit=True):
        self.instance.owner = self.request.user
        return super().save(commit)

