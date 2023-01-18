from django.db import models
from django.contrib.auth.models import User 
# Create your models here.


status_choices = [(0,'Started'),(1,'Pending'),(2,'Wroking'),(3,'Finished')]



class TaskModel(models.Model):

    class StatusChoices(models.IntegerChoices):
        Not_started = 0,"Not started"
        Started = 1 ,"Strated"
        Working = 2 ,"Working"
        Done = 3,"Done"

    task_name = models.CharField(max_length=100)
    status = models.IntegerField(choices = StatusChoices.choices)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,blank=True)
    updated_at = models.DateTimeField(auto_now_add=False,auto_now=True)
    
    def __str__(self):
        return self.task_name


class SubtaskModel(models.Model):
    sub_task_name = models.CharField(max_length=100)
    task = models.ForeignKey(TaskModel,on_delete=models.CASCADE)    
    created_date = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f'{self.task_id} {self.sub_task_name}'



