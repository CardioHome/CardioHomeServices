# -*- coding: utf-8 -*-
__author__ = ['Fung']
from __future__ import unicode_literals
from service.views import *

from django.test import TransactionTestCase


class PatientRegistration(TransactionTestCase):
    def test_patient_registration(self):
        org = Organization.objects.create(name='Patient', org_type=0)
        reg_key = generate_reg_key(0, org.pk, 0)

        key = get_reg_key(reg_key.key)

        signup('JohnDoe', 'qwerty', 'johndoe@example.com', key.key, data={'nick_name': "John", 'role': 0, 'tz': "PST"})

        token = login('JohnDoe', 'qwerty')

        user_id = get_user_id(token)

        user = get_user(user_id)

        edited_user = edit_user(user.pk, data={'nick_name': "Jim"})

        self.assertEqual(get_user(edited_user.pk).nick_name, "Jim")

        home = create_home({'name':"Jim's home",
                            'state': 0,
                            'city': 'Seattle',
                            'zip_code': '12345',
                            'address1': 'Address 1',
                            'address2': 'Address 2',
                            'size': '2000',
                            'tz': 'PST'})

        django_user = User(username="Django_Admin", password='012345')
        django_user.save()

        customer_guy = Stakeholder.objects.create(nick_name="Admin",
                                                  django_user=django_user, role=5, organization=org)
        self.assertIsNotNone(customer_guy)
        self.assertIsNotNone(user)
        self.assertIsNotNone(home)

        add_user_to_home(customer_guy.pk, user.pk, home.pk)