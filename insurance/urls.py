from django.urls import path
from . import views

urlpatterns = [  
       path('insurance/', views.InsuranceAPI.as_view()),
       path('delete/<int:pk>/', views.InsuranceDelete.as_view()),
       path('deleteall/', views.InsuranceDeleteAll.as_view()),
       path('insurancegetspecificdetails/<int:pk>/', views.Insurancegetspecificdetails.as_view()),
]  