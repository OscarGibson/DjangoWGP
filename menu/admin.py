# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Menu

class MenuAdmin(admin.ModelAdmin):
    pass
admin.site.register(Menu, MenuAdmin)
