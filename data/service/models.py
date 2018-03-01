# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



# Create your models here.

DataType = (
    (0, 'heart rate')
)

class PatientData(models.Model):
    device_uuid = models.UUIDField()
    home_id = models.IntegerField()
    data_type = models.IntegerField(choices=DataType)
    int_val1 = models.IntegerField(blank=True, null=True)
    int_val2 = models.IntegerField(blank=True, null=True)
    flt_val1 = models.FloatField(blank=True, null=True)
    flt_val2 = models.FloatField(blank=True, null=True)
    str_val = models.CharField(max_length=200)

