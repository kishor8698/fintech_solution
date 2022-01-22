from django.db import models
from datetime import datetime 
from datetime import date

COMPANY_CHOICES = [("ACKO","ACKO"),
                   ("Kotak","Kotak")
                    ]
PRODUCT_CHOICES =[("ARTH_Sanjeevni","ARTH Sanjeevni"),
                  ("ARTH_Swasth","ARTH Swasth"),
                  ("ARTH_Jeevan","ARTH Jeevan")
                  ]
OCCUPATION_CHOICES = [("Salaried","Salaried"),("Self_Employed/Business","Self Employed/Business"),("Unemployed","Unemployed"),("Student","Student")]
FAMILY_CHOICES = [("2A2C","2A2C")]
NOMINEE_DEPENDENT_CHOICES = [("Nominee","Nominee"),("Dependent","Dependent")]
RELATIONSHIP_CHOICES = [("Self","Self"),
                        ("Son","Brother"),
                        ("Father_in_Law","Father in Law"),
                        ("Brother_in_law","Brother in law"),
                        ("Father","Father"),
                        ("Husband","Husband"),
                        ("Mother","Mother"),
                        ("Daughter","Daughter"),
                        ("Wife","Wife"),
                        ("Mother_in_law","Mother-in-law"),
                        ("Daughter_in_law","Daughter-in-law"),
                        ("Sister_in_law","Sister-in-law"),
                        ("Son_in_law","Son-in-law")
                        ]
GENDER_CHOICES=[("Male","Male"),("Female","Female"),("Other","Other")]
class Insurance(models.Model):
    insurance_company=models.CharField(max_length=50,choices=COMPANY_CHOICES)
    product_type=models.CharField(max_length=50,choices=PRODUCT_CHOICES) 
    no_of_policy=models.IntegerField() #Text Box(For Sanjeevni and Swasth fix value to 1, for jeevan value should be between 1 to 5 )
    tenure=models.IntegerField()
    member_id=models.IntegerField(unique=True) #Text Box (For Sanjeevni and Swasth fix value to 12, for jeevan value should be 60)
    registration_date=models.DateField()         #auto populate
    alternate_mobile_no=models.IntegerField(unique=True)
    occupation=models.CharField(max_length=200,choices=OCCUPATION_CHOICES)
    family_type=models.CharField(max_length=200,choices=FAMILY_CHOICES)
    current_residence_state=models.TextField(max_length=500)
    current_residence_city=models.TextField(max_length=500)
    pincode=models.IntegerField()
    permanent_address=models.TextField(max_length=500)
    nominee_dependent=models.CharField(max_length=200,choices=NOMINEE_DEPENDENT_CHOICES)
    first_name=models.CharField(max_length=255)
    middle_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    mobile_no=models.IntegerField()
    date_of_birth=models.DateField()
    relationship=models.CharField(max_length=200,choices=RELATIONSHIP_CHOICES)
    gender=models.CharField(max_length=200,choices=GENDER_CHOICES)
    email_id=models.CharField(max_length=400,unique=True)
    is_delete=models.BooleanField(default=True)
    created_at=models.DateTimeField(default=datetime.now(),blank=True)    
    updated_at=models.DateTimeField(blank=True,null=True)    
 