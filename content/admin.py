# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

class ContentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Content, ContentAdmin)

class HeadingAdmin(admin.ModelAdmin):
    pass
admin.site.register(Heading, HeadingAdmin)

class TextAdmin(admin.ModelAdmin):
    pass
admin.site.register(Text, TextAdmin)

class IconAdmin(admin.ModelAdmin):
    pass
admin.site.register(Icon, IconAdmin)

class IconBlockAdmin(admin.ModelAdmin):
    pass
admin.site.register(IconBlock, IconBlockAdmin)
