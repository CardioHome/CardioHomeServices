# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from connector import dispatch
# Create your views here.
@dispatch
def get_all_product():
    pass


@dispatch
def create_transaction(sale_product, bill_info):
    pass


@dispatch
def get_transaction(transaction_id):
    pass
