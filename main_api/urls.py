from django.conf.urls import url
from django.views.static import serve
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,TokenVerifyView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('partnerapi/', include('partner_onboarding.urls')),
    path('employeeapi/', include('employee.urls')),
    path('customerapi/', include('customer_onboarding.urls')),
    path('insuranceapi/', include('insurance.urls')),
    path('insurance_p_collectionapi/', include('insurance_p_collection.urls')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
