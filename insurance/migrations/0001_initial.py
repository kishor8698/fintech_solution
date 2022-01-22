# Generated by Django 3.2.11 on 2022-01-22 06:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_company', models.CharField(choices=[('ACKO', 'ACKO'), ('Kotak', 'Kotak')], max_length=50)),
                ('product_type', models.CharField(choices=[('ARTH_Sanjeevni', 'ARTH Sanjeevni'), ('ARTH_Swasth', 'ARTH Swasth'), ('ARTH_Jeevan', 'ARTH Jeevan')], max_length=50)),
                ('no_of_policy', models.IntegerField()),
                ('tenure', models.IntegerField()),
                ('member_id', models.IntegerField(unique=True)),
                ('registration_date', models.DateField()),
                ('alternate_mobile_no', models.IntegerField(unique=True)),
                ('occupation', models.CharField(choices=[('Salaried', 'Salaried'), ('Self_Employed/Business', 'Self Employed/Business'), ('Unemployed', 'Unemployed'), ('Student', 'Student')], max_length=200)),
                ('family_type', models.CharField(choices=[('2A2C', '2A2C')], max_length=200)),
                ('current_residence_state', models.TextField(max_length=500)),
                ('current_residence_city', models.TextField(max_length=500)),
                ('pincode', models.IntegerField()),
                ('permanent_address', models.TextField(max_length=500)),
                ('nominee_dependent', models.CharField(choices=[('Nominee', 'Nominee'), ('Dependent', 'Dependent')], max_length=200)),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('mobile_no', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('relationship', models.CharField(choices=[('Self', 'Self'), ('Son', 'Brother'), ('Father_in_Law', 'Father in Law'), ('Brother_in_law', 'Brother in law'), ('Father', 'Father'), ('Husband', 'Husband'), ('Mother', 'Mother'), ('Daughter', 'Daughter'), ('Wife', 'Wife'), ('Mother_in_law', 'Mother-in-law'), ('Daughter_in_law', 'Daughter-in-law'), ('Sister_in_law', 'Sister-in-law'), ('Son_in_law', 'Son-in-law')], max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=200)),
                ('email_id', models.CharField(max_length=400, unique=True)),
                ('is_delete', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 22, 12, 29, 37, 762050))),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
