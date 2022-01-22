from django.urls import path
from . import views

urlpatterns = [  
       path('insurance_p_collection/', views.Insurance_p_collectionAPI.as_view()),
       path('delete/<int:pk>/', views.Insurance_p_collectionDelete.as_view()),
       path('deleteall/', views.Insurance_p_collectionDeleteAll.as_view()),
       path('insurance_p_collectiongetspecificdetails/<int:pk>/', views.Insurance_p_collectiongetspecificdetails.as_view()),
]