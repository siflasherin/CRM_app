from django import forms
from django.forms import widgets
from django.forms import ModelForm
from centerhead.models import Department, Employee
from crmcuser.models import MyUser


class DepartmentAddForm(ModelForm):
    class Meta:
        model = Department
        fields = ["dep_no", "name"]
        widgets = {
            "dep_no": forms.TextInput(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"})
        }
        labels = {
            "dep_no": "Department No",
            "name": "Department Name"
        }


class EmployeeAddForm(ModelForm):
    class Meta:
        model = Employee
        fields = ["emp_no", "designation", "f_name", "l_name", "phone", "email",
                  "address_1", "address_2", "city", "state", "pin", "department"]

        widgets = {
            "emp_no": forms.TextInput(attrs={"class": "form-control"}),
            "designation": forms.TextInput(attrs={"class": "form-control"}),
            "f_name": forms.TextInput(attrs={"class": "form-control"}),
            "l_name": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "pin": forms.TextInput(attrs={"class": "form-control"}),
        }

        labels = {
            "emp_no": "Employee No",
            "designation": "Designation",
            "f_name": "First Name",
            "l_name": "Last Name",
            "phone": "Phone No",
            "email": "Email",
            "address_1": "Address_1",
            "address_2": "Address_2",
            "city": "City",
            "state": "State",
            "pin": "Pin",
            "department": "Department"
        }


class AdminForm(ModelForm):
    class Meta:
        model = MyUser
        fields = ["email", "phone", "role", "password"]
        widgets = {
            "email": widgets.EmailInput(attrs={"class": "form-control"}),
            "phone": widgets.TextInput(attrs={"class": "form-control"}),
            "role": widgets.Select(attrs={"class": "form-control"}),
            "password": widgets.PasswordInput(attrs={"class": "form-control"}),
        }

class LoginForm(forms.Form):
    email=forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
