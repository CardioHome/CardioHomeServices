# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class NotificationTrigger(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    trigger_func = models.CharField(max_length=200)
    level = models.IntegerField()


class PatientTrigger(models.Model):
    trigger = models.ForeignKey(NotificationTrigger, on_delete=models.CASCADE)
    home_id = models.IntegerField()


class Notification(models.Model):
    ntf_type = models.ForeignKey(NotificationTrigger, on_delete=models.CASCADE)
    home_id = models.IntegerField()
    context = models.TextField()

