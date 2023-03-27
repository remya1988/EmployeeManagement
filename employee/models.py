from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Employee(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    emp_name=models.CharField(max_length=20)
    ph_no=models.PositiveBigIntegerField()
    emergency_no=models.PositiveBigIntegerField()
    address=models.TextField(max_length=200,null=True)
    position=models.CharField(max_length=50,null=False)
    dob=models.DateField(null=True)
    martial_status=models.CharField(max_length=10)
    blood_gp=models.CharField(max_length=10)
    job_title=models.CharField(max_length=30)
    work_location=models.CharField(max_length=40)
    date_join=models.DateField()
    reporting_to=models.CharField(max_length=30)
    linkedin=models.CharField(max_length=100)
    prof_pic=models.ImageField(upload_to="img",null=True)
    email=models.EmailField(null=True)
    password=models.CharField(max_length=100,default="")

class EmployeeLeave(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    apply_date=models.DateField(auto_now_add=True)
    nature_of_leave=models.TextField(max_length=200)
    first_day=models.CharField(max_length=20)
    last_day=models.CharField(max_length=20)
    number_of_days=models.IntegerField()
    status=models.CharField(max_length=20,default="Pending")
