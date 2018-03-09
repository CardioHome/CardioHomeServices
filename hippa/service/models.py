# -*- coding: utf-8 -*-
__author__ = ['Simon']
from __future__ import unicode_literals

from django.db import models

class BaseModel(models.Model):
    delete_time = models.DateTimeField()
    create_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)

    def encrypt(self):
        pass


    def decrypt(self):
        pass


# Create your models here.
Prefix = (
    (0, 'Dr.'),
    (1, 'Sr.')
)

class PatientInfo():
    user_id = models.IntegerField()
    age = models.IntegerField()
    gender = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    prefix = models.IntegerField(choices=Prefix)
    weight = models.FloatField()
    height = models.FloatField()
