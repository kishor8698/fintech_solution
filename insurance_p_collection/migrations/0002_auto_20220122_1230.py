# Generated by Django 3.2.11 on 2022-01-22 07:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_p_collection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurance_p_collection',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 22, 12, 30, 26, 408019)),
        ),
        migrations.AlterField(
            model_name='insurance_p_collection',
            name='payment_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 22, 12, 30, 26, 408019)),
        ),
    ]
