# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField


class BaseModel(models.Model):
    delete_time = models.DateTimeField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Device(BaseModel):
    DeviceType = (
        (0, 'electrocardiogram'),
        (1, 'smart fork'),
        (2, 'body temperature sensor'),
        (3, 'pill dispenser'),
        (4, 'stress sensor'),
        (5, 'exercise activity sensor'),
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

    def __str__(self):
        return "uuid: " + str(self.uuid) + ", Name: " + self.display_name + ", Device type: " + str(self.device_type)


class RawData(BaseModel):
    sensor = models.ForeignKey(Device, on_delete=models.CASCADE)
    data = JSONField()

    def __str__(self):
        return "uuid: " + self.sensor.uuid
