from django.db import models

# Create your models here.

class Department(models.Model):
    dep_no=models.CharField(max_length=50)
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Employee(models.Model):
    emp_no=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    address_1=models.TextField(max_length=50)
    address_2=models.TextField(max_length=50)
    city=models.CharField(max_length=50)
    options=(
        ("Andhra Pradesh","Andhra Pradesh"),
        ("Arunachal Pradesh","Arunachal Pradesh"),
        ("Assam","Assam"),
        ("Bihar","Bihar"),
        ("Chhattisgarh","Chhattisgarh"),
        ("Goa","Goa"),
        ("Gujarat","Gujarat"),
        ("Haryana","Haryana	"),
        ("Himachal Pradesh","Himachal Pradesh"),
        ("harkhand","harkhand"),
        ("Karnataka","Karnataka"),
        ("Kerala","Kerala"),
        ("Madhya Pradesh","Madhya Pradesh"),
        ("Maharashtra","Maharashtra"),
        ("Manipur","Manipur"),
        ("Meghalaya","Meghalaya"),
        ("Mizoram","Mizoram"),
        ("Nagaland","Nagaland"),
        ("Odisha","Odisha"),
        ("Punjab","Punjab"),
        ("Rajasthan","Rajasthan"),
        ("Sikkim","Sikkim"),
        ("Tamil Nadu","Tamil Nadu"),
        ("Telangana","Telangana"),
        ("Tripura","Tripura"),
        ("Uttar Pradesh","Uttar Pradesh"),
        ("Uttarakhand","Uttarakhand"),
        ("West Bengal","West Bengal")
    )
    state=models.CharField(max_length=50,choices=options,default="Kerala")
    pin=models.CharField(max_length=50)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)