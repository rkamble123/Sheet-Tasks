from django.contrib import admin
from .models import TaskModel,SubtaskModel

# Register your models here.


admin.site.register(TaskModel)
admin.site.register(SubtaskModel)