# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField


# Create your models here.
class BaseModel(models.Model):
    delete_time = models.DateTimeField()
    create_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)

DeviceType = (
    (0, 'smart fork')
)

DeviceStatus = (
    (0, 'offline')
)


class Device(BaseModel):
    display_name = models.CharField(max_length=100)
    device_type = models.IntegerField(choices=DeviceType)
    status = models.IntegerField(choices=DeviceStatus)
    home_id = models.IntegerField()
    uuid = models.UUIDField()


class RawData(BaseModel):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    data = JSONField()
