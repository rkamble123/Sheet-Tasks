from django.db import models

# Create your models here.

'''
CharField
DateField
DecimalField
DateTimeField
EmailField
ImageField
IntegerField
ForeignKey
ManyToMany
OneToOne

'''

class Employee(models.Model):
    employee = models.IntegerField()
    employee_name = models.CharField(max_length=100)
    join_date = models.DateField(auto_now_add=True)
    salary_date = models.DateTimeField()
    salary = models.DecimalField(decimal_places=3,max_digits=10)
    employee_email = models.EmailField()
    employee_image = models.ImageField(upload_to='employee-img/',blank=True)

    def __str__(self):
        return self.employee_name


class ManyToManyProject(models.Model):
    project_name = models.CharField(max_length=100)
    employee_assigned = models.ManyToManyField(Employee,blank=True)

    def __str__(self):
        return self.project_name

    

class OneToManyProject(models.Model):
    project_name = models.CharField(max_length=100)
    employee_assigned = models.OneToOneField(Employee,on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name


class ForeignProject(models.Model):
    project_name = models.CharField(max_length=100)
    Employee_assigned = models.ForeignKey(Employee,on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name