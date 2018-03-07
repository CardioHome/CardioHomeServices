# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from service.views import *

from django.test import TransactionTestCase

# Create your tests here.
class PatientRegistration(TransactionTestCase ):
    def test_patient_registration(self):
        org = Organization.objects.create(name='Patient', org_type=0)
        reg_key = generate_reg_key(0, org.pk, 0)

        key = get_reg_key(reg_key.key)

        signup('JohnDoe', 'qwerty', 'johndoe@example.com', key.key, data={'nick_name': "John", 'role': 0, 'tz': "PST"})

        user = login('JohnDoe', 'qwerty')

        get_user(user.pk)

        edited_user = edit_user(user.pk, data={'nick_name': "Jim"})

        self.assertEqual(get_user(edited_user.pk).nick_name, "Jim")

        name = models.CharField(max_length=200)
        state = models.IntegerField(choices=States)
        city = models.CharField(max_length=200)
        zip_code = models.CharField(max_length=30)
        address1 = models.CharField(max_length=200)
        address2 = models.CharField(max_length=200)
        size = models.IntegerField()
        tz = models.CharField(max_length=10)

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