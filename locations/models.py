from django.db import models

class Governorate(models.Model):
    name = models.CharField(max_length=50,unique=True)
    
    
class City(models.Model):
    name = models.CharField(max_length=50,unique=True)
    governorate = models.ForeignKey(Governorate,on_delete=models.CASCADE,related_name='cities')
    