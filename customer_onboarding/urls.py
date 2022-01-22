from django.urls import path
from . import views

urlpatterns = [
    path('customer/', views.CustomerAPI.as_view()),
    # path("employeelogin/",views.EmployeeLogin.as_view()),
    path('delete/<int:pk>', views.CustomerDelete.as_view()),
    path('deleteall/', views.CustomerDeleteAll.as_view()),
    path('customergetspecificdetails/<int:pk>', views.Customergetspecificdetails.as_view()),
]  