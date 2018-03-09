# -*- coding: utf-8 -*-
__author__ = ['Fung', 'Simon']

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


States = (
    (0, 'Alaska'),
    (1, 'Alabama'),
    (2, 'Arkansas'),
    (3, 'American Samoa'),
    (4, 'Arizona'),
    (5, 'California'),
    (6, 'Colorado'),
    (7, 'Connecticut'),
    (8, 'District of Columbia'),
    (9, 'Delaware'),
    (10, 'Florida'),
    (11, 'Georgia'),
    (12, 'Guam'),
    (13, 'Hawaii'),
    (14, 'Iowa'),
    (15, 'Idaho'),
    (16, 'Illinois'),
    (17, 'Indiana'),
    (18, 'Kansas'),
    (19, 'Kentucky'),
    (20, 'Louisiana'),
    (21, 'Massachusetts'),
    (22, 'Maryland'),
    (23, 'Maine'),
    (24, 'Michigan'),
    (25, 'Minnesota'),
    (26, 'Missouri'),
    (27, 'Northern Mariana Islands'),
    (28, 'Mississippi'),
    (29, 'Montana'),
    (30, 'National'),
    (31, 'North Carolina'),
    (32, 'North Dakota'),
    (33, 'Nebraska'),
    (34, 'New Hampshire'),
    (35, 'New Jersey'),
    (36, 'New Mexico'),
    (37, 'Nevada'),
    (38, 'New York'),
    (39, 'Ohio'),
    (40, 'Oklahoma'),
    (41, 'Oregon'),
    (42, 'Pennsylvania'),
    (43, 'Puerto Rico'),
    (44, 'Rhode Island'),
    (45, 'South Carolina'),
    (46, 'South Dakota'),
    (47, 'Tennessee'),
    (48, 'Texas'),
    (49, 'Utah'),
    (50, 'Virginia'),
    (51, 'Virgin Islands'),
    (52, 'Vermont'),
    (53, 'Washington'),
    (54, 'Wisconsin'),
    (55, 'West Virginia'),
    (56, 'Wyoming')
)


mapping = {k: v for k, v in States}


class BaseModel(models.Model):
    delete_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Home(BaseModel):
    name = models.CharField(max_length=200)
    state = models.IntegerField(choices=States)
    city = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=30)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    size = models.IntegerField()
    tz = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Organization(BaseModel):

    OrgType = (
        (0, 'None'),
        (1, 'Hospital'),
        (2, 'Insurance'),
        (3, 'Research'),
    )
    name = models.CharField(max_length=200)
    introduction = models.TextField(null=True)
    org_type = models.IntegerField(choices=OrgType)

    def __str__(self):
        return self.name


Roles = {
    (0, 'Patient'),
    (1, 'Doctor'),
    (2, 'Family member'),
    (3, 'Insurance agent'),
    (4, 'Researcher'),
    (5, 'Customer service representative')
}


class Stakeholder(BaseModel):
    nick_name = models.CharField(max_length=100, blank=False, null=False)
    avatar = models.ImageField(blank=True, null=True)
    django_user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField(choices=Roles)
    home = models.ManyToManyField(Home)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    tz = models.CharField(max_length=10)
    lang = models.CharField(max_length=10)

    def __str__(self):
        return self.nick_name


class RegisterKey(BaseModel):
    key = models.CharField(max_length=100)
    role = models.IntegerField(choices=Roles)
    organization = models.ForeignKey(Organization, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.key
