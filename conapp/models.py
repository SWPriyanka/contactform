from django.db import models

# Create your models here.
class StudentData(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.BigIntegerField()
    address=models.CharField(max_length=100)
    dob=models.DateField()