from django.db import models

# Create your models here.

class categories(models.Model):
    title = models.CharField(max_length=200)
    created_data = models.DateTimeField(auto_now_add=True,blank=True)
    updated_data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class products(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(categories,on_delete=models.CASCADE)
    created_data = models.DateTimeField(auto_now_add=True,blank=True)
    updated_data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title