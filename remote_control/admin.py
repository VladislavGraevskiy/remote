# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models.user import Userprofile
from .models.models import *

admin.site.register(Userprofile)
# admin.site.register(UserAdmin)
admin.site.register(Telemetry)
admin.site.register(Sensor)
admin.site.register(Commands)
admin.site.register(Schedule)
