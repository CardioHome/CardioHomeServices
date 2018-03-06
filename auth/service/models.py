# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


States = (
    ('AK', 'Alaska'),
    ('AL', 'Alabama'),
    ('AR', 'Arkansas'),
    ('AS', 'American Samoa'),
    ('AZ', 'Arizona'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DC', 'District of Columbia'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('GU', 'Guam'),
    ('HI', 'Hawaii'),
    ('IA', 'Iowa'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('MA', 'Massachusetts'),
    ('MD', 'Maryland'),
    ('ME', 'Maine'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MO', 'Missouri'),
    ('MP', 'Northern Mariana Islands'),
    ('MS', 'Mississippi'),
    ('MT', 'Montana'),
    ('NA', 'National'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('NE', 'Nebraska'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NV', 'Nevada'),
    ('NY', 'New York'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('PR', 'Puerto Rico'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VA', 'Virginia'),
    ('VI', 'Virgin Islands'),
    ('VT', 'Vermont'),
    ('WA', 'Washington'),
    ('WI', 'Wisconsin'),
    ('WV', 'West Virginia'),
    ('WY', 'Wyoming')
)


mapping = {k: v for k, v in States}


class BaseModel(models.Model):
    delete_time = models.DateTimeField(null=True)
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
