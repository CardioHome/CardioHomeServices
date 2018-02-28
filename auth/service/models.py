# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


State = (
    (0, 'AL'),
    (1, 'AB')
)
mapping = {k:v for k,v in State}


# Create your models here.
class BaseModel(models.Model):
    delete_time = models.DateTimeField()
    create_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)


class Home(BaseModel):
    name = models.CharField(max_length=200)
    state = models.IntegerField(choices=State)
    city = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=30)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    size = models.IntegerField()
    tz = models.CharField(max_length=10)


OrgType = (

)
class Organization(BaseModel):
    name = models.CharField(max_length=200)
    introduction = models.TextField()
    org_type = models.IntegerField(choices=OrgType)


class Stakeholder(BaseModel):
    nick_name = models.CharField(max_length=100, blank=False, null=False)
    avatar = models.ImageField(blank=True, null=True)
    django_user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField()
    home = models.ManyToManyField(Home)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    tz = models.CharField(max_length=10)
    lang = models.CharField(max_length=10)


class RegisterKey(BaseModel):
    key = models.CharField(max_length=100)
    role = models.IntegerField()
    organization = models.ForeignKey(Organization, null=True, on_delete=models.CASCADE)
