# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .models import *
from .views import *

from django.test import TransactionTestCase


# Create your tests here.
class PaymentWorkflow(TransactionTestCase):
    def test_payment_workflow(self):
        self.assertIsNone(get_all_product())

        # test add_product
        product = add_product({"display_name": "product3", "price": 30, "type": 2})
        self.assertEqual(product.display_name, "product3")
        self.assertEqual(get_all_product().count(), 1)

        product = add_product({"display_name": "product3", "price": 30, "type": 2})
        self.assertIsNone(product)
        self.assertEqual(get_all_product().count(), 1)

        # test get_product
        products = get_product("product3")
        self.assertIsNotNone(products)

        products = get_product("product10")
        self.assertIsNone(products)

        products = get_product("product1111")
        self.assertIsNone(products)

        # test edit_product
        products = edit_product({"display_name": "product1", "price": 100, "type": 0})
        self.assertIsNone(products)

        products = edit_product({"display_name": "product3", "price": 103, "type": 2})
        self.assertIsNotNone(products)
        self.assertEqual(products.count(), 1)
        self.assertEqual(products[0].price, 103)
        self.assertEqual(products[0].type, 2)

        # test create_transaction
        transaction = create_transaction({"amount": 11, "status": 21, "bill_address": "bill_address1", "order_type": 0, "credit_card_number": 12, "reference_id": 101})
        self.assertIsNotNone(transaction)
        self.assertEqual(transaction.reference_id, 101)

        transaction = create_transaction({"amount": 11, "status": 21, "bill_address": "bill_address1", "order_type": 0, "credit_card_number": 12, "reference_id": 101})
        self.assertIsNone(transaction)

        # test get_transaction
        transactions = get_transaction(101)
        self.assertIsNotNone(transactions)
        self.assertEqual(transactions.count(), 1)
        self.assertEqual(transactions[0].reference_id, '101')

        transactions = get_transaction(102)
        self.assertIsNone(transactions)

        # test edit_transaction
        transactions = edit_transaction({"amount": 11, "status": 21, "bill_address": "bill_address1", "order_type": 1, "credit_card_number": 12,"reference_id": 101})
        self.assertIsNotNone(transactions)
        self.assertEqual(transactions[0].order_type, 1)

        transactions = get_transaction(101)
        self.assertIsNotNone(transactions)
        self.assertEqual(transactions.count(), 1)
        self.assertEqual(transactions[0].order_type, 1)




