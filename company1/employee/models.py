from django.db import models

# Create your models here.

class Employee(models.Model):
    email=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    contact=models.IntegerField( default='1')

    class Meta:
        db_table='employee'