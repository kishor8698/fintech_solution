from django.urls import path
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,TokenVerifyView)


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('partner/', views.PartnerAPI.as_view()),
    path('partnerlogin/', views.PartnerLogin.as_view()),
    path('delete/<int:pk>', views.PartnerDelete.as_view()),
    path('deleteall/', views.PartnerDeleteAll.as_view()),
    path('partnergetspecificdetails/<int:pk>', views.Partnergetspecificdetails.as_view()),
    # path('partner/<int:pk>', views.PartnerAPI.as_view()),  # app homepage
]  