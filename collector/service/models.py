# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField


class BaseModel(models.Model):
    delete_time = models.DateTimeField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)


class Device(BaseModel):
    DeviceType = (
        (0, 'smart fork'),
        (1, 'pill dispenser'),
        (2, 'heart sensor'),
        (3, 'temperature sensor')
    )

    DeviceStatus = (
        (0, 'offline'),
        (1, 'online'),
    )

    display_name = models.CharField(max_length=100)
    device_type = models.IntegerField(choices=DeviceType)
    status = models.IntegerField(choices=DeviceStatus)
    home_id = models.IntegerField()
    uuid = models.UUIDField()


class RawData(BaseModel):
    sensor = models.ForeignKey(Device, on_delete=models.CASCADE)
    data = JSONField()
