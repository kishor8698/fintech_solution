from enum import unique
from django.db import models
from datetime import datetime 
from datetime import date

PAYMENT_MODE_CHOICES =[("Cash","Cash"),
                       ("NEFT","NEFT"),
                       ("IMPS","IMPS"),
                       ("UPI","UPI")]

KYC_TYPE_CHOICES =[("PAN","PAN Card"),("Voter","Voter ID"),("Driving","Driving Licence")]

class Insurance_p_collection(models.Model):
    premium_amount=models.IntegerField()
    payment_mode=models.CharField(max_length=200,choices=PAYMENT_MODE_CHOICES)
    payment_date=models.DateTimeField(default=datetime.now(),blank=True)
    transaction_no=models.CharField(max_length=400)
    account_head=models.CharField(max_length=200) # dependet field
    ac_holder_name=models.CharField(max_length=200)
    ac_no=models.CharField(max_length=400,unique=True)
    ifsc_code=models.CharField(max_length=200,unique=True)
    bank_name=models.CharField(max_length=400)
    branch_name=models.CharField(max_length=400)
    kyc_proof=models.ImageField(upload_to='Insurance_p_collection/kyc_proof/')
    kyc_type=models.CharField(max_length=200,choices=KYC_TYPE_CHOICES)
    id_number=models.IntegerField()
    bank_proof=models.ImageField(upload_to='Insurance_p_collection/bank_proof/')
    payment_receipt=models.ImageField(upload_to='Insurance_p_collection/payment_receipt/')
    is_delete=models.BooleanField(default=True)
    created_at=models.DateTimeField(default=datetime.now(),blank=True)   
    updated_at=models.DateTimeField(blank=True,null=True)