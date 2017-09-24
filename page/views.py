# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from .models import Page
from post.models import Post

templates = {
	'simple'           : 'page/index.html',
	'simple-invisible' : 'page/index-invisible.html',
	'blog'             : 'post/blog.html',
}

def index(request, slug):
	if (not(slug) or slug[0]!= '/'): slug = '/' + slug
	page = get_object_or_404(Page, slug= slug)

	context = {
		'page'  : page,
		'posts' : Post.objects.all() if page.page_type == 'blog' else []
	}
	template = templates[page.page_type]

	return render(request, template, context)