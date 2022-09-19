from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser
# from .managers import CustomUserManager
# Create your models here

class Employee(AbstractUser):
    # first_name=models.CharField(max_length=20)
    # last_name=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    # username = 
    date_of_joining=models.DateField(null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    # objects = CustomUserManager()

    # def __str__(self):
        # return self.email

    # def __str__(self):
    #     return self.first_name+self.last_name    


# class Employee(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE,
#         primary_key=True,)
#     email=models.EmailField()
#     doj=models.DateField()

class Department(models.Model):
    employee=models.OneToOneField(Employee,on_delete=models.CASCADE,
        primary_key=True,)
    department_name=models.CharField(max_length=30)

    # def __str__(self) -> str:
    #     return self.department_name

class Project(models.Model):
    employee=models.ForeignKey(Employee, on_delete=models.PROTECT, related_name="employee")
    project_name=models.CharField(max_length=30)
    project_manager_name=models.ForeignKey(Employee, on_delete=models.PROTECT, related_name="project_manager_name")
    project_manager_email=models.EmailField()
    project_start_date=models.DateField()
    project_end_date=models.DateField()

    # def __str__(self) -> str:
    #     return self.project_manager_name

    
        





        

