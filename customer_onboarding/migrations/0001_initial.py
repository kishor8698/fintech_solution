# Generated by Django 3.2.11 on 2022-01-22 06:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_onboarding_form', models.CharField(choices=[('Loan', 'Loan'), ('Insurance', 'Insurance'), ('Arthpay', 'Arthpay')], max_length=400)),
                ('mobile_no', models.IntegerField(unique=True)),
                ('customer_photo', models.ImageField(upload_to='customer/profile/')),
                ('address_proof', models.ImageField(upload_to='customer/address_proof/')),
                ('address_proof_id_number', models.IntegerField()),
                ('id_proof', models.ImageField(upload_to='customer/id_proof/')),
                ('id_proof_id_number', models.IntegerField()),
                ('full_name_mr_ms', models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms')], max_length=400)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=400, null=True)),
                ('pan', models.CharField(max_length=400, null=True)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=100)),
                ('marital_status', models.CharField(choices=[('Married', 'Married'), ('Unmarried', 'Unmarried'), ('Widowed', 'Widowed')], max_length=200)),
                ('address_type', models.CharField(choices=[('Rented', 'Rented'), ('Owned', 'Owned')], max_length=300)),
                ('current_residence_state', models.CharField(max_length=400)),
                ('current_residence_city', models.CharField(max_length=400)),
                ('pin_code', models.CharField(max_length=400)),
                ('customer_address', models.CharField(max_length=400)),
                ('customer_address_landmark', models.CharField(max_length=400, null=True)),
                ('is_delete', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 1, 22, 12, 28, 37, 261486))),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
