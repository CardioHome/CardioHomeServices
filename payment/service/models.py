# -*- coding: utf-8 -*-
__author__ = ['Simon']
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField

import uuid

class BaseModel(models.Model):
    delete_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)


Status = (
    (0, 'pending'),
    (1, 'successful'),
    (2, 'failed')
)


OrderType = (
    (0, 'patient basic'),
    (1, 'patient premium'),
    (2, 'clinic basic'),
    (3, 'clinic premium')
)


class SaleProduct(BaseModel):
    display_name = models.CharField(max_length=100)
    price = models.IntegerField()
    type = models.IntegerField(choices=OrderType)

    def __str__(self):
        return self.display_name


# Create your models here.
class Transaction(BaseModel):
    transaction_id = models.UUIDField(default=uuid.uuid4)
    credit_card_number = models.CharField(max_length=100)
    reference_id = models.CharField(max_length=100)
    amount = models.IntegerField()
    status = models.IntegerField(choices=Status)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bill_address = JSONField()
    order_type = models.IntegerField(choices=OrderType)

    def __str__(self):
        return "reference_id: " + str(self.reference_id)