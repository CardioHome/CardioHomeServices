# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Home, Organization, Stakeholder, RegisterKey

admin.site.register(Home)
admin.site.register(Organization)
admin.site.register(Stakeholder)
admin.site.register(RegisterKey)
