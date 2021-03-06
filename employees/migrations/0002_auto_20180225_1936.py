# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-25 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=25),
        ),
        migrations.AlterField(
            model_name='employees',
            name='marital_status',
            field=models.CharField(choices=[('Single', 'Single'), ('Married', 'Married')], max_length=25),
        ),
        migrations.AlterField(
            model_name='employees',
            name='position',
            field=models.CharField(choices=[('Employee', 'Employee'), ('Manager', 'Manager'), ('CEO', 'CEO')], max_length=25),
        ),
    ]
