# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class BaseModel(models.Model):
    delete_time = models.DateTimeField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)


class PatientData(BaseModel):

    DataType = (
        (0, 'heart rate'),
        (1, 'nutritional intake'),
        (2, 'body temperature'),
        (3, 'medication intake')
        (4, 'stress level'),
        (5, 'exercise activity'),
    )

    device_uuid = models.UUIDField()
    home_id = models.IntegerField()
    data_type = models.IntegerField(choices=DataType)
    int_val1 = models.IntegerField(blank=True, null=True)
    int_val2 = models.IntegerField(blank=True, null=True)
    flt_val1 = models.FloatField(blank=True, null=True)
    flt_val2 = models.FloatField(blank=True, null=True)
    str_val = models.CharField(max_length=200)
    device_create_time = models.DateTimeField()

    def __str__(self):
        return "uuid: " + str(self.device_uuid) + ", data type: " + str(self.data_type)
