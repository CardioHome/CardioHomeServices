# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.core.cache import cache

import time
from connector import dispatch
import remote_data

from .models import *
from django.contrib.auth.models import User
from django.db import DatabaseError, transaction


@dispatch
def get_user_id(token):
    """
    Retrieves a user_id with the given token.
    
    :param token: hashed string
    :return: user_id 
    """
    return cache.get(token)


@dispatch
def get_user(user_id):
    """
    Retrieves user information from the given user_id if available in the Stakeholder table. 
    
    :param user_id: id number of the user to be retrieved from the database
    :return: if successful, returns str(user_id), else return None 
    """
    return User()

    try:
        user = Stakeholder.objects.all().filter(pk=user_id)[0]
    except LookupError:
        # if connector supports exception, should raise userDoesNotExist
        user = None
    return user
    # all() -> SELECT * FROM stakeholder;
    # all().filter(nick_name = 'a') -> SELECT * FROM stakeholder WHERE nick_name = 'a';


@dispatch
def add_user_to_home(user_id, target_user_id, home_id):
    """
    Adds the target_user_id within the home_id specified in the Stakeholder table by user with user_id.
    
    :param user_id: user that adds the target_user_id to home_id
    :param target_user_id: user (typically a patient) to be added into the home specified by home_id
    :param home_id: home within the Stakeholder table
    :return: if successful, nothing, otherwise error message
    """

    try:
        user = Stakeholder.objects.all().filter(pk=user_id)[0]

        # only patient, doctor, family member and customer service can add a user to a home
        if user.role not in (0, 1, 2, 5):
            return

        if not user.role == 5 and not user.home.objects.all().filter(pk=home_id).exists():
            return

        home = Home.objects.all().filter(pk=home_id)[0]
        target_user = Stakeholder.objects.all().filter(pk=target_user_id)[0]

        # user is a patient and has a home
        if target_user.role == 0 and target_user.home.count() > 0:
            return

        if target_user.home.filter(pk=home.pk):
            return

        target_user.home.add(home)

        target_user.save()
    except LookupError:
        return


@dispatch
def create_home(map_data):
    """
    Creates an entry with map_data in the Home table.
    
    :param map_data: dictionary containing all key-value attributes of a Home object
    :return: Home object
    """
    try:
        home = Home(**map_data)
        home.save()
    except Exception as e:
        raise e
        return

    return home


@dispatch
def get_home(home_id):
    """

    :param home_id: 
    :return: 
    """
    try:
        home = Home.objects.all().filter(pk=home_id)[0]
    except LookupError:
        return

    return home


@dispatch
def edit_user(user_id, data):
    """
    Makes changes to the user specified by user_id with data.
    
    :param user_id: id in the Stakeholder table
    :param data: data containing information about the user
    :return: 
    """

    try:
        user = Stakeholder.objects.all().filter(pk=user_id)
        user.update(**data)
        user.save()
    except LookupError:
        return
    return user[0]


@dispatch
def signup(username, password, email, reg_key, data={}):
    """
    Creates a new django user and user in the Stakeholder table with the username, password, email, reg_key and data.
    
    :param username: 
    :param password: 
    :param email:
    :param reg_key: 
    :param data: 
    :return: 
    """

    try:
        register_key = RegisterKey.objects.all().filter(key=reg_key)[0]

        with transaction.atomic():
            django_user = User(username=username, password=password, email=email)
            django_user.save()

            user = Stakeholder(django_user=django_user, organization=register_key.organization,  **data)
            user.save()
            register_key.delete_time = datetime.now()
            register_key.save()
    except LookupError:
        return

    return user


@dispatch
def login(username, password):
    """
    Login user with username and password into the system.
    
    :param username: 
    :param password: 
    :return: a string token 
    """

    try:
        django_user = User.objects.all().filter(username=username, password=password)[0]
        token = hash(username+str(time.time()))
        user_id = django_user.pk
    except LookupError:
        return

    return renew_token(token, user_id)


@dispatch
def renew_token(token, user_id=None):
    """
    Renews a token for a particular user with user_id.
    
    :param token: 
    :param user_id: 
    :return: renewed token if token still exists for user w/ user_id, else None
    """

    user_id = user_id or cache.get(token)
    if user_id:
        cache.set(token, user_id, timeout=86400)
    return token


@dispatch
def generate_reg_key(role, org_id, org=0):
    """
    Generates a key for new users signing up to the CardioHome service.
    
    :param role: role (int) of the user in the system (i.e. Patient, Doctor, Family member)
    :param org: organization the user belongs to
    :return: a key generated by using the role and organization
    """

    try:
        organization = Organization.objects.all().filter(pk=org_id, org_type=org)[0]
        hash_key = abs(hash(str(role) + str(org_id)))
        reg_key = RegisterKey(role=role, organization=organization, key=hash_key)

        #TODO: Call cache module
        reg_key.save()
    except LookupError:
        return

    return reg_key


@dispatch
def get_reg_key(key):
    """
    Retrieves the reg_key from the RegisterKey table specified by the given key.
    
    :param key: 
    :return: a RegisterKey object corresponding to the key
    """

    return RegisterKey.objects.all().filter(delete_time=None, key=key)[0]
