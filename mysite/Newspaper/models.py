from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=10, decimal_places=2)