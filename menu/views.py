# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Menu

def menu_view():
	return render('', 'menu.menu.html', {})
