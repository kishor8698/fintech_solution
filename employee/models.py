from msilib.schema import Class
from pyexpat import model
from django.db import models
from datetime import datetime 
from datetime import date

BRANCH_CHOICES =[("Bachhrawan","Bachhrawan"),("Barabanki","Barabanki"),
                 ("Bhiwadi","Bhiwadi"), ("Faizabad","Faizabad"),
                 ("Lucknow","Lucknow"),("Madiyon","Madiyon"),
                 ("Pataudi","Pataudi"),("Raebareli","Raebareli"),
                 ("Sultanpur","Sultanpur"),("Tijara","Tijara"),
                 ("Unchahar","Unchahar"),("Unnao","Unnao")]

MARTIAL_status_CHOICES=[("Married","Married"),("Unmarried","Unmarried"),("Widowed","Widowed")]    
QUALIFICATION_CHOICES =[("No_Formal_Education","No Formal Education"),
                        ("Primary_Education","Primary Education"),
                        ("Secondary_Education","Secondary Education or High School"),
                        ("General_Educational_Development","General Educational Development"),
                        ("Vocational_Qualifiacation","Vocational Qualifiacation"),
                        ("Bachelor_Degree","Bachelor's Degree"),
                        ("Master_Degree","Master's Degree"),
                        ("Doctorate_or_Higher","Doctorate or Higher"),
                        ]

GENDER_CHOICES =[("Male","Male"),("Female","Female"),("Other","Other")]
DEPARTMENT_CHOICES =[("Operations","Operations"),
                     ("HR","HR"),
                     ("IT","IT"),
                     ("Accounts","Accounts"),
                     ("Kalpatru","Kalpatru"),
                     ("Director","Director"),
                     ("Management","Management"),
                     ("MIS","MIS"),
                     ("Finance","Finance"),
                     ("Marketing_&_Communications","Marketing & Communications"),
                     ("Audit_&_Compliance","Audit & Compliance"),
                     ("Collections","Collections"),
                     ("Products","Products"),
                     ("Policy_&_Advocacy","Policy & Advocacy")
                     ]

ROLE_CHOICES =[("CLC","CLC"),
               ("CLO","CLO"),
               ("CLM","CLM"),
               ("OM","OM")
               ]
class Bank_Branches(models.Model):
    bank_branches=models.CharField(max_length=255)
    
class Employee(models.Model):
    # @property
    # def val_ucic(self):
    #     branch=self.branch
    #     branch=branch[:3].upper()
    #     if Employee.objects.all()==0:
    #         return branch+str('001')
    #     else:
    #         last_ucic=Employee.objects.last()
    #         value=int(last_ucic.user_name_employee_ucic[3:])+1
    #         return value
    
    branch=models.ForeignKey(Bank_Branches, on_delete=models.CASCADE,related_name='brankToemployess')
    employee_name=models.CharField(max_length=200)
    date_of_birth=models.DateField()
    marital_status=models.CharField(max_length=200,choices=MARTIAL_status_CHOICES)
    qualification=models.CharField(max_length=200,choices=QUALIFICATION_CHOICES)
    gender=models.CharField(max_length=100,choices=GENDER_CHOICES)
    guargian_name=models.CharField(max_length=400)
    guargian_mo_number=models.IntegerField(unique=True)
    personal_email_id=models.CharField(max_length=400,unique=True)
    office_email_id=models.CharField(max_length=400,unique=True)
    date_of_joining=models.DateField()
    religion=models.CharField(max_length=400)
    state=models.CharField(max_length=400)
    district=models.CharField(max_length=400)
    permanent_address=models.TextField(max_length=500)
    pincode=models.IntegerField()
    corresponding_address=models.TextField(max_length=500)
    department=models.CharField(max_length=255,choices=DEPARTMENT_CHOICES)
    designation=models.CharField(max_length=255)
    grade=models.CharField(max_length=255)
    blood_group=models.CharField(max_length=255)
    uan=models.CharField(max_length=255)
    reporting_officer=models.CharField(max_length=255)
    emp_bank=models.CharField(max_length=255)    #<-----------
    bank_branch=models.CharField(max_length=255) #<-----------
    bank_address=models.TextField(max_length=255)
    bank_account_no=models.IntegerField(unique=True)
    ifsc=models.CharField(max_length=255,unique=True)
    pan_no=models.CharField(max_length=255,unique=True)
    address_proof=models.ImageField(upload_to='employee/address_proof/')
    id_proof=models.ImageField(upload_to='employee/id_proof/')
    photo=models.ImageField(upload_to='employee/photo/')
    role=models.CharField(max_length=255,choices=ROLE_CHOICES)
    # user_name_employee_ucic=models.CharField(max_length=255,,default=val_ucic)
    user_password=models.CharField(max_length=255)
    multiple_branch=models.ManyToManyField(Bank_Branches,related_name='branchesToemployees')
    is_delete=models.BooleanField(default=True)
    created_at=models.DateTimeField(default=datetime.now())    
    updated_at=models.DateTimeField(blank=True,null=True) 
    

