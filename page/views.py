# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from .models import Page

templates = {
	'simple'           : 'page/index.html',
	'simple-invisible' : 'page/index-invisible.html',
}

def index(request, slug):
	if not(slug): slug = '/'
	page = get_object_or_404(Page, slug= slug)

	context = {
		'page' : page
	}
	template = templates[page.page_type]

	return render(request, template, context)