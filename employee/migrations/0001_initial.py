# Generated by Django 3.2.11 on 2022-01-22 06:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank_Branches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_branches', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField()),
                ('marital_status', models.CharField(choices=[('Married', 'Married'), ('Unmarried', 'Unmarried'), ('Widowed', 'Widowed')], max_length=200)),
                ('qualification', models.CharField(choices=[('No_Formal_Education', 'No Formal Education'), ('Primary_Education', 'Primary Education'), ('Secondary_Education', 'Secondary Education or High School'), ('General_Educational_Development', 'General Educational Development'), ('Vocational_Qualifiacation', 'Vocational Qualifiacation'), ('Bachelor_Degree', "Bachelor's Degree"), ('Master_Degree', "Master's Degree"), ('Doctorate_or_Higher', 'Doctorate or Higher')], max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=100)),
                ('guargian_name', models.CharField(max_length=400)),
                ('guargian_mo_number', models.IntegerField(unique=True)),
                ('personal_email_id', models.CharField(max_length=400, unique=True)),
                ('office_email_id', models.CharField(max_length=400, unique=True)),
                ('date_of_joining', models.DateField()),
                ('religion', models.CharField(max_length=400)),
                ('state', models.CharField(max_length=400)),
                ('district', models.CharField(max_length=400)),
                ('permanent_address', models.TextField(max_length=500)),
                ('pincode', models.IntegerField()),
                ('corresponding_address', models.TextField(max_length=500)),
                ('department', models.CharField(choices=[('Operations', 'Operations'), ('HR', 'HR'), ('IT', 'IT'), ('Accounts', 'Accounts'), ('Kalpatru', 'Kalpatru'), ('Director', 'Director'), ('Management', 'Management'), ('MIS', 'MIS'), ('Finance', 'Finance'), ('Marketing_&_Communications', 'Marketing & Communications'), ('Audit_&_Compliance', 'Audit & Compliance'), ('Collections', 'Collections'), ('Products', 'Products'), ('Policy_&_Advocacy', 'Policy & Advocacy')], max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('grade', models.CharField(max_length=255)),
                ('blood_group', models.CharField(max_length=255)),
                ('uan', models.CharField(max_length=255)),
                ('reporting_officer', models.CharField(max_length=255)),
                ('emp_bank', models.CharField(max_length=255)),
                ('bank_branch', models.CharField(max_length=255)),
                ('bank_address', models.TextField(max_length=255)),
                ('bank_account_no', models.IntegerField(unique=True)),
                ('ifsc', models.CharField(max_length=255, unique=True)),
                ('pan_no', models.CharField(max_length=255, unique=True)),
                ('address_proof', models.ImageField(upload_to='employee/address_proof/')),
                ('id_proof', models.ImageField(upload_to='employee/id_proof/')),
                ('photo', models.ImageField(upload_to='employee/photo/')),
                ('role', models.CharField(choices=[('CLC', 'CLC'), ('CLO', 'CLO'), ('CLM', 'CLM'), ('OM', 'OM')], max_length=255)),
                ('user_password', models.CharField(max_length=255)),
                ('is_delete', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 1, 22, 12, 29, 19, 831970))),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brankToemployess', to='employee.bank_branches')),
                ('multiple_branch', models.ManyToManyField(related_name='branchesToemployees', to='employee.Bank_Branches')),
            ],
        ),
    ]
