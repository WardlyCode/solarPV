from django.db import models

# Create your models here.
from django.db import models

class Client(models.Model):
    FirstName = models.CharField(max_length=30) 
    LastName = models.CharField(max_length=30)
    Location = models.CharField(max_length=30) 

class Location(models.Model):
    Name = models.CharFieldmax_length=30
    ZipCode = models.CharField(max_length=30)

class Product(models.Model):
    Name = models.CharField(max_length=30)
    Client = models.CharField(max_length=30)
    

class TestStandard(models.Model):
    Name = models.CharField(max_length=30)
    ID = models.CharField(max_length=30)


class Certificate(models.Model):
    Product = models.CharField(max_length=30)
    ID = models.CharField(max_length=30)
    Client = models.CharField(max_length=30)
    Location = models.CharField(max_length=30)

