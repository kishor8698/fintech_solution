from django.db import models
from datetime import datetime 
from datetime import date

CUSTOMER_ONBOARDING_FORM_CHOICES = [("Loan","Loan"),("Insurance","Insurance"),("Arthpay","Arthpay")]
MR_MS_CHOICES =[("Mr","Mr"),("Mrs","Mrs"),("Ms","Ms")]
GENDER_CHOICES =[("Male","Male"),("Female","Female"),("Other","Other")]
MARTIAL_status_CHOICES=[("Married","Married"),("Unmarried","Unmarried"),("Widowed","Widowed")]    
ADDRESS_TYPE_CHOICES = [("Rented","Rented"),("Owned","Owned")]

class Customer(models.Model):
    customer_onboarding_form=models.CharField(max_length=400,choices=CUSTOMER_ONBOARDING_FORM_CHOICES)
    mobile_no=models.IntegerField(unique=True)
    customer_photo=models.ImageField(upload_to='customer/profile/')
    address_proof=models.ImageField(upload_to='customer/address_proof/')
    address_proof_id_number=models.IntegerField() #fetch from OCR
    id_proof=models.ImageField(upload_to='customer/id_proof/')
    id_proof_id_number=models.IntegerField()  #fetch from OCR
    full_name_mr_ms=models.CharField(choices=MR_MS_CHOICES,max_length=400)
    firstname=models.CharField(max_length=255)  #Fetch from ID Proof
    lastname=models.CharField(max_length=255)   #Fetch from ID Proof
    email=models.CharField(max_length=400,null=True)
    pan=models.CharField(max_length=400,null=True) # fetch from OCR
    date_of_birth=models.DateField() # fetch from OCR
    gender=models.CharField(max_length=100,choices=GENDER_CHOICES)
    marital_status=models.CharField(max_length=200,choices=MARTIAL_status_CHOICES)
    address_type=models.CharField(max_length=300,choices=ADDRESS_TYPE_CHOICES)
    current_residence_state=models.CharField(max_length=400) #fetch from Adress proof
    current_residence_city=models.CharField(max_length=400) #fetch from Adress proof
    pin_code=models.CharField(max_length=400) #fetch from Adress proof
    customer_address=models.CharField(max_length=400) #fetch from Adress proof
    customer_address_landmark=models.CharField(max_length=400,null=True)
    is_delete=models.BooleanField(default=True)
    created_at=models.DateTimeField(default=datetime.now())    
    updated_at=models.DateTimeField(blank=True,null=True)
    # kyc=models.CharField(max_length=400)# autofetch from kyc