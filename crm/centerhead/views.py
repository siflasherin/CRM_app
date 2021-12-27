from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import CreateView, ListView, UpdateView, DetailView, TemplateView
from centerhead.models import Department, Employee
from centerhead.forms import DepartmentAddForm, EmployeeAddForm, AdminForm, LoginForm
from django.urls import reverse_lazy
from crmcuser.models import MyUser
from django.utils.decorators import method_decorator
from centerhead.decorators import signin_required
from django.contrib.auth import logout, authenticate, login


def home(request):
    return render(request, "home.html")


@method_decorator(signin_required, name="dispatch")
class AddDepartment(CreateView):
    model = Department
    form_class = DepartmentAddForm
    template_name = "add_dept.html"
    success_url = reverse_lazy("addemployee")


@method_decorator(signin_required, name="dispatch")
class AddEmployee(CreateView):
    model = Employee
    form_class = EmployeeAddForm
    template_name = "add_employee.html"
    success_url = reverse_lazy("listemployee")


@method_decorator(signin_required, name="dispatch")
class ListEmployee(ListView):
    model = Employee
    template_name = "list_employee.html"
    context_object_name = "employees"


@method_decorator(signin_required, name="dispatch")
class ViewEmployee(DetailView):
    model = Employee
    template_name = "view_employee.html"
    pk_url_kwarg = "id"


@method_decorator(signin_required, name="dispatch")
class UpdateEmployee(UpdateView):
    model = Employee
    form_class = EmployeeAddForm
    template_name = "update_employee.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("listemployee")


@method_decorator(signin_required, name="dispatch")
class RemoveEmployee(TemplateView):
    def get(self, request, *args, **kwargs):
        id = kwargs["id"]
        employee = Employee.objects.get(id=id)
        employee.delete()
        return redirect("listemployee")


class CreateAdmin(CreateView):
    model = MyUser
    form_class = AdminForm
    template_name = "admin_create.html"
    success_url = reverse_lazy("adminsignin")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            emp = MyUser.objects.create_user(email=employee.email, phone=employee.phone, role=employee.role,
                                             password=employee.password)
            emp.save()

        return redirect("adminsignin")


class SignIn(TemplateView):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        context = {}
        context["form"] = form
        return render(request, "adminlogin.html", context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            # if given credentials are valid ,return a user object
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                if (request.user.role == "admin"):
                    return redirect("listemployee")
                else:
                    return redirect("adminsignin")
            else:
                return redirect("adminsignin")
        else:
            return redirect("adminsignin")


@signin_required
def signout(request, *args, **kwargs):
    logout(request)
    return redirect("adminsignin")
