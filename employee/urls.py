from django.urls import path
from . import views

urlpatterns = [  
    path('employee/', views.EmployeeAPI.as_view()),
    path("employeelogin/",views.EmployeeLogin.as_view()),
    path('delete/<int:pk>', views.EmployeeDelete.as_view()),
    path('deleteall/', views.EmployeeDeleteAll.as_view()),
    path('employeegetspecificdetails/<int:pk>', views.Employeegetspecificdetails.as_view()),
]  