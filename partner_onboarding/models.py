from django.db import models
from datetime import datetime 
from datetime import date
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import UserManager,PermissionsMixin
# from django.contrib.auth.models import 
# Create your models here.
CHOICES=[('YES','YES'),
         ('NO','NO')]
    
class Partner(models.Model):
# class Partner(AbstractBaseUser,PermissionsMixin):
    mobile=models.IntegerField(unique=True)
    kyc_poi=models.ImageField(upload_to='partner_onbarding/',unique=True)
    kyc_poa=models.ImageField(upload_to='partner_onbarding/',unique=True)
    shop_owner_photo=models.ImageField(upload_to='partner_onbarding/profile_pic')
    shop_photo_with_owner=models.ImageField(upload_to='partner_onbarding/shop_photo_with_owner')
    shop_front_photo=models.ImageField(upload_to='partner_onbarding/shop_front_photo')
    lat_long=models.IntegerField()
    shop_name=models.CharField(max_length=200)
    other_documents=models.FileField(upload_to='partner_onbarding/other_documents',null=True)
    name_of_partners1=models.CharField(max_length=200)
    name_of_partners2=models.CharField(max_length=200)
    address=models.CharField(max_length=400)
    similar_address=models.CharField(max_length=400,choices=CHOICES)
    email_id=models.CharField(max_length=200,unique=True)
    alternate_mo_no=models.IntegerField()
    business_category=models.CharField(max_length=400)
    number_of_merchants=models.IntegerField()
    annual_income=models.IntegerField()
    no_of_employees =models.IntegerField()
    aadhaar_cibil=models.CharField(max_length=300)
    locations_covered=models.IntegerField() 
    bank_ifsc=models.CharField(max_length=400)
    bank_account_number=models.IntegerField(unique=True) 
    bank_account_name=models.CharField(max_length=400)
    bank_name=models.CharField(max_length=400)
    additional_comments=models.TextField(max_length=500,null=True)
    digital_agreement=models.IntegerField()
    is_delete=models.BooleanField(default=True)
    created_at=models.DateTimeField(default=datetime.now(),blank=True)    
    updated_at=models.DateTimeField(blank=True,null=True) 
    approve_reject=models.BooleanField(default=False)  
    password=models.CharField(max_length=255)
    # partner_ucic=models.CharField(max_length=255,) # Query
    digital_agreement=models.BooleanField(default=False) 
 
#     USERNAME_FIELD = 'email_id'
#     REQUIRED_FIELDS = []
#     objects = UserManager()

#     class Meta:
#         verbose_name = 'user'
#         verbose_name_plural = 'users'
#         db_table = u'partner_onboarding_partner'
        
# class UserManager(BaseUserManager):
#     def create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError("The email must be set")
#         if not password:
#             raise ValueError("The password must be set")
#         email = self.normalize_email(email)

#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user
    
#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_active', True)
#         extra_fields.setdefault('role', 'Admin')

#         if extra_fields.get('role') != 'Admin':
#             raise ValueError('Superuser must have role of Global Admin')
#         return self.create_user(email, password, **extra_fields)