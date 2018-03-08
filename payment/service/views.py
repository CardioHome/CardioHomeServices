# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.shortcuts import render

from connector import dispatch

from .models import *

import json

from django.forms.models import model_to_dict

# Create your views here.
@dispatch
def get_all_product():
    """
    get all products from database
    :return all products:
    """
    try:
        all_products = SaleProduct.objects.all()
        if not all_products.exists():
            return
        return all_products
    except LookupError:
        return "LookupError when getting all products"


@dispatch
def add_product(map_data):
    """
    Get product by display name
    :param map_data: Dictionary of all members in the product
    :return product:
    """
    try:
        display_name = map_data.get("display_name")
        if not display_name:
            print("display_name is None")
            return
        if SaleProduct.objects.all().filter(display_name=display_name).exists():
            print("product "+display_name + " already exists")
            return
        product = SaleProduct(**map_data)
        product.save()
        return product
    except LookupError:
        print("LookupError when adding product: " + display_name)


@dispatch
def edit_product(map_data):
    """
    edit existing product
    :param map_data: Dictionary of some members in the product
    :return product
    """
    try:
        display_name = map_data["display_name"]
        if not display_name:
            print("display_name is None")
            return
        product = SaleProduct.objects.all().filter(display_name=display_name)
        if not product.exists():
            print("product "+display_name + " does not exist")
            return
        product.update(**map_data)
        product[0].save()
        return product
    except LookupError:
        print("LookupError when editing product: " + display_name)


@dispatch
def get_product(display_name):
    """
    Get product by display_name
    :param display_name: product name
    :return: product
    """
    try:
        product = SaleProduct.objects.all().filter(display_name=display_name)
        if not product.exists():
            print("product "+display_name + " does not exist")
            return
        return product
    except LookupError:
        print("LookupError when getting product: " + display_name)


@dispatch
def create_transaction(map_data):
    """
    Create a transaction
    :param map_data: Dictionary of all members in the transaction
    :return: transaction
    """
    try:
        reference_id = map_data.get("reference_id")
        if reference_id is None:
            print("reference_id is None")
            return
        if Transaction.objects.all().filter(reference_id=reference_id).exists():
            print("reference "+str(reference_id) + " already exists")
            return
        transaction = Transaction(**map_data)
        transaction.save()
        return transaction
    except LookupError:
        print("LookupError when creating transaction: reference_id: " + str(reference_id))


@dispatch
def get_transaction(reference_id):
    """
    Get a transaction by id
    :param reference_id: reference id
    :return: transaction
    """
    try:
        transaction = Transaction.objects.all().filter(reference_id=reference_id)
        if not transaction.exists():
            print("Transaction " + str(reference_id) + " does not exist")
            return
        return transaction
        # return "Get transaction: "+ str(transaction[0].reference_id)
    except LookupError:
        print("LookupError when getting transaction: " + str(reference_id))
