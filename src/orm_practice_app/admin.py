from django.contrib import admin
from .models import Employee,ManyToManyProject,ForeignProject,OneToManyProject
# Register your models here.

admin.site.register(Employee)
admin.site.register(ManyToManyProject)
admin.site.register(ForeignProject)
admin.site.register(OneToManyProject)