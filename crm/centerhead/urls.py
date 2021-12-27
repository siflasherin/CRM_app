from django.urls import path
from centerhead import views

urlpatterns = [
    path("", views.home, name="home"),
    path("dept/add/", views.AddDepartment.as_view(), name="adddept"),
    path("employee/add/", views.AddEmployee.as_view(), name="addemployee"),
    path("employee/list/", views.ListEmployee.as_view(), name="listemployee"),
    path("employee/view/<int:id>", views.ViewEmployee.as_view(), name="viewemployee"),
    path("employee/update/<int:id>", views.UpdateEmployee.as_view(), name="updateemployee"),
    path("employee/remove/<int:id>", views.RemoveEmployee.as_view(), name="removeemployee"),
    path("createadmin/", views.CreateAdmin.as_view(), name="createadmin"),
    path("adminsignin/", views.SignIn.as_view(), name="adminsignin"),
    path("adminsignout/", views.signout, name="adminsignout"),

]
