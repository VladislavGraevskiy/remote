# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from remote.study.models.user import Userprofile

admin.site.register(Userprofile, UserAdmin)
